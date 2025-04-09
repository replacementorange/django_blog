from django.db import models


'''
Post's category model. Contains category's name.
'''
class Category(models.Model):
    name = models.CharField(max_length=30)


'''
Post's model. Contains title, body, time when created and 
last modified. Creates a relationship between a post and categories.
'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


'''
Post's comment model. Contains comment's author, comment,
time when created. Defines many-to-one relationship between
comment (many) and post (one). When post is deleted comment(s)
are also deleted.
'''
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)