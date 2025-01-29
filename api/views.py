from app.models import products
from .serializers import Productserializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .pagination import paginationTwo
class Postapi(ListCreateAPIView):
    pagination_class = paginationTwo
    permission_classes = (IsAuthenticated,)
    queryset = products.objects.all()
    serializer_class = Productserializers

class AllApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = products.objects.all() 
    serializer_class = Productserializers
  
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from app.models import *
# from .serializers import Productserializers

# @api_view(['GET', 'POST', 'DELETE']) 
# def Postview(request):
#     if request.method == 'GET':
#         post = products.objects.all()
#         serializers = Productserializers(post, many=True)
#         return Response(serializers.data )
#     if request.method == 'POST':
#         ser = Productserializers(data = request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response({'error' : 'xato'})
    
# @api_view(['GET', 'DELETE', 'PUT']) 
# def DeleteVeiw(request, pk):
#     try:
#         a = products.objects.get(id=pk)
#     except:
#         return Response({'xato' : 'Ushbu user mavjud emas'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializers = Productserializers(a)
#         return Response(serializers.data )
#     if request.method == 'DELETE':
#         a.delete()
#         return Response({'message' : 'O\'chirildi'}, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         ser = Productserializers(a, data = request.data)
#         if ser.is_valid():
#             ser.save() 
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response({'error' : 'xato'})