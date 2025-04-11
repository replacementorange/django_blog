from django.test import TestCase
from django.utils import timezone

from blog.models import Category, Post, Comment


class CategoryTest(TestCase):
    """Tests for the Category model"""

    def create_category(self, name="test category"):
        return Category.objects.create(name=name)


    def test_category_creation(self):
        """
        Creates a Category object and tests whether the created 
        name matched the expected name.
        """
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)


    def test_category_plural_name(self):
        """
        Tests whether the plural name of the Category model is 'categories'.
        """
        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")


class PostTest(TestCase):
    """Tests for the Post model"""

    def create_post(self, title="test title", body="test body", categories=None):
        post = Post.objects.create(title=title, body=body, created_on=timezone.now())
        if categories:
            post.categories.set(categories)
        return post


    def test_post_creation(self):
        """
        Creates a Post object and tests whether the created 
        title and body matched the expected values.
        """

        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), "test title")
        self.assertEqual(post.body, "test body")


    def test_post_category_relationship(self):
        """
        Tests the many-to-many relationship between Post and Category.
        """

        category1 = Category.objects.create(name="Category 1")
        category2 = Category.objects.create(name="Category 2")
        post = self.create_post(categories=[category1, category2])
        self.assertEqual(post.categories.count(), 2)
        self.assertIn(category1, post.categories.all())
        self.assertIn(category2, post.categories.all())


class CommentTest(TestCase):
    """Tests for the Comment model"""

    def create_comment(self, author="test author", body="test comment", post=None):
        if post is None:
            post = Post.objects.create(title="test post", body="test body")
        return Comment.objects.create(author=author, body=body, post=post)


    def test_comment_creation(self):
        """
        Creates a Comment object and tests whether the created 
        author and body matched the expected values.
        """

        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), f"{comment.author} on '{comment.post}'")
        self.assertEqual(comment.body, "test comment")


    def test_comment_post_relationship(self):
        """
        Tests the foreign key relationship between Comment and Post.
        """

        post = Post.objects.create(title="test post", body="test body")
        comment = self.create_comment(post=post)
        self.assertEqual(comment.post, post)


    def test_comment_deletion_on_post_delete(self):
        """
        Tests that comments are deleted when the related post is deleted.
        """

        post = Post.objects.create(title="test post", body="test body")
        comment = self.create_comment(post=post)
        post.delete()
        self.assertEqual(Comment.objects.filter(id=comment.id).count(), 0)


    def test_comment_creation(self):
        """
        Creates a Comment object and tests whether the created 
        author and body matched the expected values.
        """

        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), f"{comment.author} on '{comment.post}'")
        self.assertEqual(comment.body, "test comment")
