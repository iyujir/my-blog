from django.db import models
from db.base_model import BaseModel
from ckeditor.fields import RichTextField


# Create your models here.


class Links(BaseModel):
    '''友情链接类'''
    name = models.CharField(max_length=40, verbose_name='链接名字')
    urls_link = models.CharField(max_length=120, verbose_name='链接地址')
    index = models.SmallIntegerField(default=0, verbose_name='权重值')  # 越大在越前面
    desc = models.CharField(max_length=120, null=True, blank=True, verbose_name='简单描述')  # 简单描述
    note = RichTextField(blank=True, null=True, verbose_name='备注')   # 备注

    class Meta:
        db_table = 'blog_links'


class AboutInfo(BaseModel):
    '''关于我介绍'''
    p = models.TextField(verbose_name='一段文字')
    index = models.SmallIntegerField(default=0, verbose_name='权重值')  # 越大在越前面
    desc = models.CharField(max_length=120, null=True, blank=True, verbose_name='简单描述')  # 简单描述
    note = RichTextField(blank=True, null=True, verbose_name='备注')   # 备注

    class Meta:
        db_table = 'blog_aboutinfo'


class AboutWork(BaseModel):
    '''工作经历'''
    company = models.CharField(max_length=40, verbose_name='公司')
    urls_link = models.CharField(max_length=120, verbose_name='公司地址')
    index = models.SmallIntegerField(default=0, verbose_name='权重值')  # 越大在越前面
    job = models.CharField(max_length=120, null=True, blank=True, verbose_name='岗位')  # 岗位描述
    start_time = models.DateField(verbose_name='开始时间')   # 工作开始时间
    end_time = models.DateField(blank=True, null=True, verbose_name='结束时间')  # 结束时间
    note = RichTextField(blank=True, null=True, verbose_name='备注')   # 备注

    class Meta:
        db_table = 'blog_aboutwork'


class AboutProject(BaseModel):
    '''项目简介'''
    name = models.CharField(max_length=40, verbose_name='项目名字')
    urls_link = models.CharField(max_length=120, verbose_name='项目地址')
    start_time = models.DateField(verbose_name='开始时间')   # 工作开始时间
    end_time = models.DateField(blank=True, null=True, verbose_name='结束时间')  # 结束时间
    index = models.SmallIntegerField(default=0, verbose_name='权重值')  # 越大在越前面
    desc = models.CharField(max_length=120, null=True, blank=True, verbose_name='项目描述')  # 简单描述
    note = RichTextField(blank=True, null=True, verbose_name='备注')   # 备注

    class Meta:
        db_table = 'blog_aboutproject'
