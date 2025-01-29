from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contac, name='contac'),
    path('shop-single/<slug:slug>/', shop_single ,name = 'shop-single'),
    path('shop/', shop, name='shop'),
    path('category1/<slug:slug>/', categoryVeiw, name='category'),
    path('category2/<slug:slug>/', category2Veiw, name='category2'),
    path('category3/<slug:slug>/', category3Veiw, name='category3'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('fourite/', fourite, name='fourite'),
    path('add_fourite/<slug:slug>/', addfourite, name='fourite1'),
    path('delete-fourite/<int:product_id>/', delete_fourite, name='delete-fourite'),
    path('bascet/', bascet1, name='bascet'),
    path('delete_bascet/<int:product_id>/', delete_bascet, name='delete_bascet')
]

