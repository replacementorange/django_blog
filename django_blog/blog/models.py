from django.db import models


class Category(models.Model):
    """
    Post's category model. Contains category's name.
    """

    name = models.CharField(max_length=30)

    # class to control the plural name of the class
    class Meta:
        verbose_name_plural = "categories"

    # String representation of object
    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post's model. Contains title, body, time when created and 
    last modified. Creates a relationship between a post and categories.
    """

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    # String representation of object
    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Post's comment model. Contains comment's author, comment,
    time when created. Defines many-to-one relationship between
    comment (many) and post (one). When post is deleted comment(s)
    are also deleted.
    """

    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    # String representation of object
    def __str__(self):
        return f"{self.author} on '{self.post}'"