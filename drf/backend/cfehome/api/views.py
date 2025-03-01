import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):  
    """ This is DRF API VIEW """   
    # if request.method != "POST":
    #       return Response({"detail":"GET not allowed"}, status=405)
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
    # instance= Product.objects.all().order_by("?").first()
    # data  ={}
    # if instance:
    #     # data = model_to_dict (instance, fields=['id', 'title', 'price', 'sale_price'])          # is same as write the query 1-by-1 as below
    #  data = ProductSerializer(instance).data
        return Response(serializer.data)

        # json_data_str = json.dumps(data) 
        # data['id'] = model_data.id
        # data ['title'] = model_data.title
        # data ['content'] = model_data.content
        # data ['price'] = model_data.price
    # return HttpResponse(data, headers={"content-type":"application/json"}) 
