# Generated by Django 2.1.7 on 2019-04-08 01:58

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190408_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='Abstract',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]