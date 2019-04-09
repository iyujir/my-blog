from django.urls import path, re_path
from home.views import IndexView, ArchivesView, LinkView, AboutView
from django.conf.urls import url


urlpatterns = [
    path('archives/', ArchivesView.as_view(), name='archives'),  # archives归档
    path('link/', LinkView.as_view(), name='link'),  # link 链接
    path('about/', AboutView.as_view(), name='about'),  # about 关于我
    re_path(r'^index(\d*)/$', IndexView.as_view()),  # index 主页
    path('', IndexView.as_view(), name='index'),  # index 主页

]

