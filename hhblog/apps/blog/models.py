from django.db import models

# Create your models here.
from users.models import User


class MyBlog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='用户id')
    title = models.CharField(max_length=50,verbose_name="标题")
    content = models.TextField(verbose_name="文章内容")
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    read = models.IntegerField(default=0, verbose_name='阅读量')
    comment = models.IntegerField(default=0, verbose_name='评论量')


    class Meta:
        db_table = 'tb_blog'
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name