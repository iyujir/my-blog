# Generated by Django 2.1.7 on 2019-04-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190409_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinfo',
            name='p',
            field=models.TextField(verbose_name='一段文字'),
        ),
    ]