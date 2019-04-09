from django.shortcuts import render, HttpResponse
from django.views.generic import View
from article.models import ArticlePost
# Create your views here.


# /article/1
class ArticleView(View):
    '''文章显示'''
    def get(self, request, article_id):
        '''显示文章'''
        page = ArticlePost.objects.get(id=article_id)
        prev_id = article_id + 1
        ident_id = article_id - 1
        # 获取文章的最大id
        id = ArticlePost.objects.all().order_by('-id')
        max_id = id[0].id
        max_id = 8
        print(max_id, '最大的值', type(max_id))
        ident_page = None
        prev_page = None
        while True:
            try:
                prev_page = ArticlePost.objects.get(id=prev_id)
            except ArticlePost.DoesNotExist:
                if prev_id >= 8:
                    break
                prev_id += 1
            else:
                break

        while True:
            try:
                ident_page = ArticlePost.objects.get(id=ident_id)
            except ArticlePost.DoesNotExist:
                if ident_id <= 1:
                    break
                ident_id -= 1

            else:
                break
        return render(request, 'article.html', {'page': page, 'ident_page': ident_page, 'prev_page': prev_page})
