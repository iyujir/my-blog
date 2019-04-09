from django.contrib import admin
from home.models import Links, AboutInfo, AboutWork, AboutProject

# Register your models here.


class LinksAdmin(admin.ModelAdmin):
    list_display = ['name']


class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ['p']


class AboutWorkAdmin(admin.ModelAdmin):
    list_display = ['company']


class AboutProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Links, LinksAdmin)

admin.site.register(AboutInfo, AboutInfoAdmin)

admin.site.register(AboutWork, AboutWorkAdmin)

admin.site.register(AboutProject, AboutProjectAdmin)


