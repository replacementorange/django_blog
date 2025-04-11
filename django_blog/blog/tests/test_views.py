from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Comment, Category
from blog.forms import CommentForm


class BlogIndexViewTests(TestCase):
    """Tests for the blog_index view"""

    def setUp(self):
        """
        Set up test posts for testing the blog_index view.
        """

        self.post1 = Post.objects.create(title="Post 1", body="Body 1")
        self.post2 = Post.objects.create(title="Post 2", body="Body 2")


    def test_blog_index_view_status_code(self):
        """
        Test that the blog_index view returns a 200 status code.
        """

        response = self.client.get(reverse("blog_index"))
        self.assertEqual(response.status_code, 200)


    def test_blog_index_view_template_used(self):
        """
        Test that the blog_index view uses the correct template.
        """

        response = self.client.get(reverse("blog_index"))
        self.assertTemplateUsed(response, "blog/index.html")


    def test_blog_index_view_context_data(self):
        """
        Test that the blog_index view provides the correct context data.
        """

        response = self.client.get(reverse("blog_index"))
        self.assertIn(self.post1, response.context["posts"])
        self.assertIn(self.post2, response.context["posts"])


class BlogCategoryViewTests(TestCase):
    """Tests for the blog_category view"""

    def setUp(self):
        """
        Set up test posts and categories for testing the blog_category view.
        """

        self.category = Category.objects.create(name="Test Category")
        self.post1 = Post.objects.create(title="Post 1", body="Body 1")
        self.post1.categories.add(self.category)
        self.post2 = Post.objects.create(title="Post 2", body="Body 2")


    def test_blog_category_view_status_code(self):
        """
        Test that the blog_category view returns a 200 status code for a valid category.
        """

        response = self.client.get(reverse("blog_category", kwargs={"category": self.category.name}))
        self.assertEqual(response.status_code, 200)


    def test_blog_category_view_template_used(self):
        """
        Test that the blog_category view uses the correct template.
        """

        response = self.client.get(reverse("blog_category", kwargs={"category": self.category.name}))
        self.assertTemplateUsed(response, "blog/category.html")


    def test_blog_category_view_context_data(self):
        """
        Test that the blog_category view provides the correct context data.
        """

        response = self.client.get(reverse("blog_category", kwargs={"category": self.category.name}))
        self.assertIn(self.post1, response.context["posts"])
        self.assertNotIn(self.post2, response.context["posts"])


class BlogDetailViewTests(TestCase):
    """Tests for the blog_detail view"""

    def setUp(self):
        """
        Set up a test post and comments for testing the blog_detail view.
        """

        self.post = Post.objects.create(title="Test Post", body="Test Body")
        self.comment = Comment.objects.create(
            author="Test Author", body="Test Comment", post=self.post
        )
        self.url = reverse("blog_detail", kwargs={"pk": self.post.pk})


    def test_blog_detail_view_status_code(self):
        """
        Test that the blog_detail view returns a 200 status code for a valid post.
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


    def test_blog_detail_view_template_used(self):
        """
        Test that the blog_detail view uses the correct template.
        """

        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "blog/detail.html")


    def test_blog_detail_view_context_data(self):
        """
        Test that the blog_detail view provides the correct context data.
        """

        response = self.client.get(self.url)
        self.assertEqual(response.context["post"], self.post)
        self.assertIn(self.comment, response.context["comments"])
        self.assertIsInstance(response.context["form"], CommentForm)


    def test_blog_detail_view_post_comment(self):
        """
        Test that a valid comment can be posted to the blog_detail view.
        """

        data = {"author": "New Author", "body": "New Comment"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # redirects after successful POST
        self.assertTrue(
            Comment.objects.filter(author="New Author", body="New Comment").exists()
        )


    def test_blog_detail_view_invalid_comment(self):
        """
        Test that an invalid comment does not get saved.
        """

        data = {"author": "", "body": "Invalid Comment"}  # missing author
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # re-renders the page
        self.assertFalse(Comment.objects.filter(body="Invalid Comment").exists())
        self.assertIn(self.comment, response.context["comments"])
        self.assertIsInstance(response.context["form"], CommentForm)


    def test_blog_detail_view_post_comment(self):
        """
        Test that a valid comment can be posted to the blog_detail view.
        """

        data = {"author": "New Author", "body": "New Comment"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # redirects after successful POST
        self.assertTrue(
            Comment.objects.filter(author="New Author", body="New Comment").exists()
        )


    def test_blog_detail_view_invalid_comment(self):
        """
        Test that an invalid comment does not get saved.
        """

        data = {"author": "", "body": "Invalid Comment"}  # author is missing
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # re-renders the page
        self.assertFalse(Comment.objects.filter(body="Invalid Comment").exists())
