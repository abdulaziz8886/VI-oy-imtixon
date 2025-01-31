from rest_framework import serializers
from app.models import *

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'
    
class Bascetselializers(serializers.ModelSerializer):
    class Meta:
        model = bascet
        fields = '__all__'

class FouriteSelializers(serializers.ModelSerializer):
    class Meta:
        model = like
        fields = '__all__'
    
class Category1Selializers(serializers.ModelSerializer):
    class Meta:
        model = categorygander
        fields = '__all__'
    
class Category2Selializers(serializers.ModelSerializer):
    class Meta:
        model = categorySale
        fields = '__all__'

class Category3Selializers(serializers.ModelSerializer):
    class Meta:
        model = categoryProduct
        fields = '__all__'

class Razmerlar_Selializers(serializers.ModelSerializer):
    class Meta:
        model = categoryRazmer
        fields = "__all__"

class Ranglar_selializers(serializers.ModelSerializer):
    class Meta:
        model = categoryRang
        fields = "__all__"


    




class about_selializers(serializers.ModelSerializer):
    class Meta:
        model = abdoutUs
        fields = '__all__'

class brands_selializers(serializers.ModelSerializer):
    class Meta:
        model = brands
        fields = '__all__'

class services_selializers(serializers.ModelSerializer):
    class Meta:
        model = services
        fields = '__all__'


class zay_first_selializers(serializers.ModelSerializer):
    class Meta:
        model = zay_first
        fields = '__all__'

class zay_second_selializers(serializers.ModelSerializer):
    class Meta:
        model = zay_second
        fields = '__all__'

class zay_second_text_selializars(serializers.ModelSerializer):
    class Meta:
        model = zay_second_text
        fields = '__all__'

class zay_third_text_selializers(serializers.ModelSerializer):
    class Meta:
        model = zay_third_text
        fields = '__all__'

class zay_third_selializers(serializers.ModelSerializer):
    class Meta:
        model = zay_third
        fields = '__all__'

  