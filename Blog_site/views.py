from django.shortcuts import render, get_object_or_404
from Blog_site.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request, author_username=None):
    posts = Post.objects.filter(status=True)
    if author_username:
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts, 3)
    try:
        pagr_number = request.GET.get('page')
        posts = posts.get_page(pagr_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    content = {'posts': posts}
    return render(request, 'our-blog.html', content)


def blog_single(request, pid):
    posts = get_object_or_404(Post, pk=pid, status=True)
    contex = {'posts': posts}
    return render(request, 'blog-details-2.html', contex)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    content = {'posts': posts}
    return render(request, 'our-blog.html', content)
