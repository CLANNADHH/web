from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class VipMessage(models.Model):
    vip_name = models.CharField(max_length=30,verbose_name="留言者")
    content = RichTextField(verbose_name="留言内容")
    message_time = models.DateTimeField(auto_now_add=True, )

    class Meta:
        db_table = "tb_message"
        verbose_name = "留言板"
        verbose_name_plural = verbose_name
