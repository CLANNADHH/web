from django.db import models

# Create your models here.
from users.models import User
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

class MyBlog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='用户id')
    title = models.CharField(max_length=50,verbose_name="标题")
    content = RichTextField(verbose_name="文章内容")
    # content = models.TextField(verbose_name="文章内容")
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    read = models.IntegerField(default=0, verbose_name='阅读量')
    comment = models.IntegerField(default=0, verbose_name='评论量')
    digest = models.TextField(verbose_name="文章摘要")
    # desc_detail = RichTextUploadingField(default='', verbose_name='详细介绍')
    # desc_pack = RichTextField(default='', verbose_name='包装信息')
    # desc_service = RichTextUploadingField(default='', verbose_name='售后服务')

    class Meta:
        db_table = 'tb_blog'
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name