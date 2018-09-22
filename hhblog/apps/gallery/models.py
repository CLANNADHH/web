from django.db import models

# Create your models here.
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.urls import reverse


class Album(models.Model):
    title = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG',
    options = {'quality': 90})
    is_visible = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(max_length=50, blank=True)
    class Meta():
        verbose_name = '图片'
    def get_absolute_url(self):

        return reverse('gallery:album_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):

        return self.title


class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG',
    options = {'quality': 70})
    thumb = ProcessedImageField(upload_to='albums/thumbs/', processors=[ResizeToFit(300)], format='JPEG',
    options = {'quality': 80}, blank = True, null = True)
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default='', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.alt
