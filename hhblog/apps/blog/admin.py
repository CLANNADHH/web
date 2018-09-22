from django.contrib import admin

# Register your models here.

from blog.models import MyBlog


class BlogInfoView(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(MyBlog, BlogInfoView)