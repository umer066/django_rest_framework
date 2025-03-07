# from algoliasearch_django import AlgoliaIndex
# from algoliasearch_django.decorators import register

# from .models import Product

# @register(Product)    
#       # this register is same as we register the models in admin.py 

# class ProductIndex(AlgoliaIndex):
#     model = Product
#     fields = [

#         'title',
#         'body',
#         'price',
#         'user',
#         'public',
        #   'path',

#     ]

    # settings = {
    #     'searchableAttributes': ['title', 'body'],
    #     'attributesForFaceting': ['user', 'public' ]
    #   }
#     tags = 'get_tags_list'