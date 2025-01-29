from django.urls import path, re_path
# from .views import Postview, DeleteVeiw, Postapi, AllApi
from .views import Postapi, AllApi
from .documentation import schema_view

urlpatterns = [
    path('', Postapi.as_view(), name='post_home'),
    path('action/<int:pk>/', AllApi.as_view(), name='allapi'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
 