from django import template
from Blog_site.models import Post, Category

register = template.Library()


@register.filter
def snippet(txt, arg=20):
    return txt[:arg] + '...'


@register.inclusion_tag('latest.html')
def latest(arg=4):
    posts = Post.objects.filter(status=True).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('category.html')
def postcategories():
    posts = Post.objects.filter(status=True)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
