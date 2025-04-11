from django.test import TestCase

from blog.forms import CommentForm


class CommentFormTest(TestCase):
    """Tests for the CommentForm"""


    def test_valid_form(self):
        """
        Tests whether the form is valid when provided with valid data.
        """

        form_data = {"author": "test author", "body": "test comment"}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_invalid_form_missing_author(self):
        """
        Tests whether the form is invalid when the author field is missing.
        """
        
        form_data = {"body": "test comment"}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("author", form.errors)


    def test_invalid_form_missing_body(self):
        
        """
        Tests whether the form is invalid when the body field is missing.
        """
        form_data = {"author": "test author"}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("body", form.errors)
