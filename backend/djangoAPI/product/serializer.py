from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=('pk','name','content','price','my_discount')
        
    def get_my_discount(self,obj):
        return obj.get_discount
        