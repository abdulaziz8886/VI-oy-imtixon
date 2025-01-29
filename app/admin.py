from django.contrib import admin

from .models import comentuser, categorygander, products, categoryProduct, categorySale, categoryRang, categoryRazmer

@admin.register(comentuser)
class ComentUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'izoh']

@admin.register(categorygander)
class CategoryGander(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug" : ('name',)}

@admin.register(categorySale)
class CategorySale(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug" : ('name',)}

@admin.register(categoryProduct)
class CategoryProduct(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug" : ('name',)}

@admin.register(categoryRazmer)
class categoryRazmer(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(categoryRang)
class categoryRazmer1(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(products)
class Product(admin.ModelAdmin):
    list_display = ['id','title', 'rasm', 'category', 'category1', "category2"]
    prepopulated_fields = {'slug' : ('title',)}
