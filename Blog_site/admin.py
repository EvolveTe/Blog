from django.contrib import admin
from Blog_site.models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'views', 'status', 'created_date', 'updated_date', 'published_date')
    list_filter = ('status', 'author',)
    # ordering = ('-created_date',)
    search_fields = ('title', 'author', 'content')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
