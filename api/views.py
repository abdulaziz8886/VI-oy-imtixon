from app.models import *
from .serializers import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .pagination import paginationTwo
class Postapi(ListAPIView):
    pagination_class = paginationTwo
    permission_classes = (IsAuthenticated,)
    queryset = products.objects.all()
    serializer_class = Productserializers

class AllApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = products.objects.all() 
    serializer_class = Productserializers


class bascet_postapi(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = bascet.objects.all()
    serializer_class = Bascetselializers

class bascet_action(RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdminUser,)
    queryset = bascet.objects.all()
    serializer_class = Bascetselializers

class fourites_postapi(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = like.objects.all()
    serializer_class = FouriteSelializers

class Fourite_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = like.objects.all()
    serializer_class = FouriteSelializers

class Category1_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = categorygander.objects.all()
    serializer_class = Category1Selializers

class Category1_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = categorygander.objects.all()
    serializer_class = Category1Selializers 


class Category2_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = categorySale.objects.all()
    serializer_class = Category2Selializers


class Category2_actions(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = categorySale.objects.all()
    serializer_class = Category2Selializers



    
class Category3_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = categorySale.objects.all()
    serializer_class = Category3Selializers


class Category3_actions(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = categorySale.objects.all()
    serializer_class = Category3Selializers



class RanglarApi(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = categoryRang.objects.all()
    serializer_class = Ranglar_selializers


class RanglarApi_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = categoryRang.objects.all()
    serializer_class = Ranglar_selializers


class razmerlar_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = categoryRazmer.objects.all()
    serializer_class = Razmerlar_Selializers



class Razmerlar_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = categoryRazmer.objects.all()
    serializer_class = Razmerlar_Selializers














class about_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = abdoutUs.objects.all()
    serializer_class = about_selializers



class about_actions(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = abdoutUs.objects.all()
    serializer_class = about_selializers




class brand_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = brands.objects.all()
    serializer_class = brands_selializers



class brand_actions(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = brands.objects.all()
    serializer_class = brands_selializers




class services_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = services.objects.all()
    serializer_class = services_selializers



class services_actions(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = services.objects.all()
    serializer_class = services_selializers



class zay_first_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = zay_first.objects.all()
    serializer_class = zay_first_selializers



class zay_first_api_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = zay_first.objects.all()
    serializer_class = zay_first_selializers




class zay_second_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = zay_first
    serializer_class = zay_second_selializers



class zay_second_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = zay_first.objects.all()
    serializer_class = zay_second_selializers




class zay_second_text_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = zay_second_text.objects.all()
    serializer_class = zay_second_text_selializars

class zay_second_text_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = zay_second_text.objects.all()
    serializer_class = zay_second_text_selializars



class zay_third_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = zay_third.objects.all()
    serializer_class = zay_third_selializers


class zay_third_action(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = zay_third.objects.all()
    serializer_class = zay_third_selializers



class zay_third_text_api(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = zay_third_text.objects.all()
    serializer_class = zay_third_text_selializers



class zay_third_text_action(RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAdminUser, )
    queryset = zay_third_text.objects.all()
    serializer_class = zay_third_text_selializers