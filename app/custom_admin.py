from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *

class SecondAdmin(AdminSite):
    site_header = 'Second Admin Panel'
    site_title = 'Second Admin'

second_admin_site = SecondAdmin(name='secondadmin')


class BlogSecondAdmin(admin.ModelAdmin):
    list_display = ('title',)
class zay_second_text1(admin.ModelAdmin):
    list_display = ['title']
class zay_second1(admin.ModelAdmin):
    ...
class zay_third_text1(admin.ModelAdmin):
    list_display = ('title',)
class zay_third1(admin.ModelAdmin):
    list_display = ('title','price', 'pre_title')




class about(admin.ModelAdmin):
    list_display = ['izoh',]

class serivices1(admin.ModelAdmin):
    list_display = ['title',]

class brands1(admin.ModelAdmin):
    ...





second_admin_site.register(zay_first, BlogSecondAdmin)
second_admin_site.register(zay_second_text, zay_second_text1)
second_admin_site.register(zay_second, zay_second1)
second_admin_site.register(zay_third_text, zay_third_text1)
second_admin_site.register(zay_third, zay_third1)
second_admin_site.register(abdoutUs, about)
second_admin_site.register(services, serivices1)
second_admin_site.register(brands, brands1)


