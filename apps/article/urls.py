from django.urls import path, re_path
from apps.article.views import ArticleView

urlpatterns = [
    path('<int:article_id>/', ArticleView.as_view(), name='article'),  # article浏览
]
