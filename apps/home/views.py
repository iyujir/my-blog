from django.shortcuts import render, HttpResponse
from django.views.generic import View
from article.models import ArticlePost
from home.models import Links, AboutInfo, AboutWork, AboutProject
from django.core.paginator import Paginator
import datetime

# Create your views here.


# /index
class IndexView(View):
    '''主页'''
    def get(self, request, pindex='1'):
        pindex = int(pindex)
        contacts_list = ArticlePost.objects.all().order_by('id')
        paginator = Paginator(contacts_list, 6)
        contacts = paginator.page(pindex)
        return render(request, 'index.html', {'contacts': contacts})


# /archives
class ArchivesView(View):
    '''归档'''
    def get(self, request):
        '''显示归档页面'''
        year = datetime.datetime.now().year
        archives_list = list()

        while year >= 2018:
            this_year = ArticlePost.objects.filter(create_time__year=year)
            for i in range(12, 0, -1):
                pages = this_year.filter(create_time__month=i).order_by('-create_time')
                if pages:
                    temp_month_list = list()
                    for page in pages:
                        temp_month_list.append(page)
                    archives_list.append(((year, i), temp_month_list))
                    # return HttpResponse(temp_month_list)
            year -= 1

            # return HttpResponse(archives_list)

        return render(request, 'archives.html', {'archives_list': archives_list})


# /link
class LinkView(View):
    '''Link 链接'''
    def get(self, request):
        '''显示友情链接页面'''
        links = Links.objects.all().order_by('-index', '-id')
        return render(request, 'link.html', {'links': links})


# /about
class AboutView(View):
    '''about 链接'''
    def get(self, request):
        '''显示友情链接页面'''
        infos = AboutInfo.objects.all().order_by('index', '-id')
        works = AboutWork.objects.all().order_by('start_time')
        projects = AboutProject.objects.all().order_by('index', 'start_time')
        return render(request, 'about.html', {'infos': infos, 'works': works, 'projects': projects})
