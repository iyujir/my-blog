from django.contrib import admin
from article.models import ArticlePost
# Register your models here.


class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


admin.site.register(ArticlePost, ArticlePostAdmin)
