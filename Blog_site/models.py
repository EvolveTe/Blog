from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(default='default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = jmodels.jDateTimeField(auto_now_add=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'POST'

    def __str__(self):
        return "{} - {}".format(self.title, self.id)


def snippets(self):
    return self.content[:100] + '...'
