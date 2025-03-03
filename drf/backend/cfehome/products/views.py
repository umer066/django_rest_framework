from rest_framework import generics, mixins

from rest_framework.response import Response
from .models import Product

from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404 

from api.mixins import StaffEditorPermissionMixin

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
    ):
    """ creating apiview """
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer 

    def perform_create(self, serializer): 
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView,
    ):
    """ reteriving apiview """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

# class ProductlistAPIView(generics.ListAPIView):
#     """ reteriving apiview """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductlistAPIView.as_view()


class ProductMixinView( mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):             # HTTP get method
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing some stuff"
        serializer.save(content=content)
 
product_mixin_view = ProductMixinView.as_view()



@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):   
    method = request.method 

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        #list view  
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView,
    ):
    """ reteriving apiview """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEditorPermissionMixin, 
    generics.DestroyAPIView,
    ):
    """ reteriving apiview """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # using instance
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()