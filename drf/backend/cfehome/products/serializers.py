from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    # my_discount  =serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
          )
    # email = serializers.EmailField(write_only = True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title ])
    name = serializers.CharField(source='title', read_only = True)
    email = serializers.CharField(source='user.email', read_only = True)
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'pk',
            'name',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user 
    #     qs = Product.objects.filter(title_iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value    
    
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance , validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)
    
    def get_url(self, obj):

        # return f"/api/v2/products/{obj.pk}/"
        request = self.content.get('request')
        if request is None:
            return None 
        return reverse ("product-detail", kwargs={"pk": obj.pk}, request = request)
    
    def get_edit_url(self, obj):
        pass

        # # return f"/api/v2/products/{obj.pk}/"
        # # request = self.content.get('request')
        # if request is None:
        #     return None 
        # url = reverse("product-edit", kwargs={"pk": obj.pk})
        # return request.build_absolute_uri(url)
        
        
        # return reverse ("product-edit", kwargs={"pk": obj.pk}, request = request)
    
    # def get_my_discount(self, obj):
    #     return obj.get_discount()