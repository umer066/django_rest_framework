from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    #  url = serializers.HyperlinkedIdentityField(
    #      view_name = 'product-detail',
    #      lookup_field = 'pk',
    #      read_only = True
    #  )
    
    title = serializers.CharField(read_only = True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only = True)  
    other_products = serializers.SerializerMethodField(read_only = True)

    def get_other_products(self , obj):       
        # obj = [            
                #  {'prod_no': 1,
                #   'flavor':[
                #   {'flavor': 'orange',
                #    'rate_list':[{
                #     'small_pack': '50rs'},
                #     {'medium_pack': '110rs'},
                #     {'large_pack': '180rs'}]},
                #   {'flavor': 'mango'},
                #   {'flavor': 'apple'},
                #   {'flavor': 'peach'}]},
                # {'prod_no': 2},
                # {'prod_no': 3},
                # {'prod_no': 4}      

        # ]
        print(obj)
        user = obj
        my_product_qs = user.product_set.all()
        return UserProductInlineSerializer(my_product_qs, many=True).data