from django.urls import path, re_path
# from .views import Postview, DeleteVeiw, Postapi, AllApi
from .views import *
from .documentation import schema_view, schema_view1

urlpatterns = [
    path('products/', Postapi.as_view(), name='post_home'),
    path('products_action/<int:pk>/', AllApi.as_view(), name='allapi'),
    path('bascet/', bascet_postapi.as_view()),
    path('bascet_action/<int:pk>/', bascet_action.as_view()),
    path('fourites/', fourites_postapi.as_view()),
    path('fourites_action/<int:pk>/', Fourite_action.as_view()),
    path('category1/', Category1_api.as_view()),
    path('category1_action/<int:pk>/', Category1_action.as_view()),
    path('category2/', Category2_api.as_view()),
    path('category2_action/<int:pk>/', Category2_actions.as_view()),
    path('category3/', Category3_api.as_view()),
    path('category3_action/<int:pk>/', Category3_actions.as_view()),
    path('ranglar/', RanglarApi.as_view()),
    path('ranglar_action/<int:pk>/', RanglarApi_action.as_view()),
    path('razmerlar/', razmerlar_api.as_view()),
    path('razmerlar_action/<int:pk>/', Razmerlar_action.as_view()),



    path('about/', about_api.as_view()),
    path('about_action/<int:pk>/', about_actions.as_view()),
    path('brands/', brand_api.as_view()),
    path('brands_action/<int:pk>/', brand_actions.as_view()),
    path('services/', services_api.as_view()),
    path('services_action/<int:pk>/', services_actions.as_view()),
    path('zay_first/', zay_first_api.as_view()),
    path('zay_first_action/<int:pk>/', zay_first_api_action.as_view()),
    path('zay_second/', zay_second_api.as_view()),
    path('zay_second_action/<int:pk>/', zay_second_action.as_view()),
    path('zay_second_text/', zay_second_text_api.as_view()),
    path('zay_second_text_action/<int:pk>/', zay_second_text_action.as_view()),
    path('zay_third/' , zay_third_api.as_view()),
    path('zay_third_action/<int:pk>/', zay_third_action.as_view()),
    path('zay_third_text/', zay_third_text_api.as_view()),
    path('zay_third_text_action/<int:pk>/', zay_third_text_action.as_view()),
    



    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger2/', schema_view1.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui1'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
 