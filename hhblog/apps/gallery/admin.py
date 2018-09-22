from django.contrib import admin

# Register your models here.

from gallery.models import Album


class GalleryInfoView(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(Album, GalleryInfoView)