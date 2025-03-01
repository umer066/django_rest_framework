from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # my_discount  =serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
          )
    edit_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    def get_url(self, obj):

        # return f"/api/v2/products/{obj.pk}/"
        request = self.content.get('request')
        if request is None:
            return None 
        return reverse ("product-detail", kwargs={"pk": obj.pk}, request = request)
    def get_edit_url(self, obj):

        # return f"/api/v2/products/{obj.pk}/"
        request = self.content.get('request')
        if request is None:
            return None 
        return reverse ("product-edit", kwargs={"pk": obj.pk}, request = request)
    
    # def get_my_discount(self, obj):
    #     return obj.get_discount()