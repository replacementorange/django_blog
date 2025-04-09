from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm


def blog_index(request):
    """
    Display a list of all posts. Obtains a queryset containing 
    all the posts in the database, arranges the objects 
    according to the argument given. Define a context dictionary 
    and render a template named index.html.
    """

    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)

def blog_category(request, category):
    """
    Display posts in the given category. Filter returns
    posts whose categories contain the corresponding category name.
    Add posts and the category to the context dictionary and render 
    a template named category.html.
    """

    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    """
    Displays the full post. Requesting a single post with the specific 
    primary key that is provided. Retrieves all the comments assigned
    to the given post. If there is none comments, then the QuerySet is
    empty. Add post and comments to the context dictionary and render
    a template named detail.html.

    Makes an instance of comment form, checks if it receives a POST request.
    If receives, updates form with the data of the POST request, 
    validates the form with .is_valid. After that saves the form and redirects
    the user to the path_info.
    """

    post = Post.objects.get(pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)