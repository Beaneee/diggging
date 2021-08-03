from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Post, Folder, CustomFolder
from . import models
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(request, "posts/post_list.html", ctx)


def post_detail(request, pk):
    details = Post.objects.get(pk=pk)
    # 댓글기능도 끌어와야함.
    ctx = {
        "details": details
        # 여기에도 댓글 넣어주어야함.
    }
    return render(request, """'html 넣어주세요'""", ctx)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save()
            posts.save()
            return redirect("""'url 넣어주세요'""")
    else:
        form = PostForm()
        ctx = {
            "form": form,
        }

        return render(request, """'html 넣어주세요'""", ctx)


def post_update(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect("post:post_detail", pk)
    else:
        form = PostForm(instance=posts)
        ctx = {
            "form": form,
        }
        return render(request, """'html 넣어주세요'""", ctx)


def post_delete(request, pk):
    posts = Post.objects.get(pk=pk)
    posts.delete()
    return redirect("""'url 넣어주세요'""")


def make_folder(request):
    folder = Post.objects.filter(request.language)
    ctx = {
        "folder":folder
    }
    return render(request, "posts/base.html",ctx)