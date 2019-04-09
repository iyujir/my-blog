from django.db import models
from db.base_model import BaseModel
from user.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ArticlePost(BaseModel):
    '''文章模型类'''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)  # 评论
    title = models.CharField(max_length=100)  # 标题
    abstract_non = models.TextField(blank=True)  # 不带格式摘要
    Abstract = RichTextField(blank=True)  # 摘要
    body = RichTextUploadingField(blank=True)  # 内容


    class Meta:
        db_table = 'blog_article'
