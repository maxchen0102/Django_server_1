import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pip._vendor.rich import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from product.models import Product

# from .serializers import ItemSerializer


# Create your views here.
#
# @api_view(['GET'])
# def getdata(request):
#     items=Product.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)
# @csrf_exempt
# @api_view(['POST'])
# def add_data(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data, )
# @csrf_exempt
# @api_view(['DELETE',"PUT","GET"])
# def delete_data(request,id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=404)
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=201)
#     elif request.method == 'PUT' :
#         serializer = ItemSerializer(instance=product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else :
#             return Response(serializer.errors,)
#     elif request.method == 'GET':
#         serializer = ItemSerializer(instance=product)
#         return Response(status=status.HTTP_404_NOT_FOUND)


# # 取得資料by id
# def get_product(request,id):
#     print("this")
#     if id :
#         product=Product.objects.get(id=id)
#         data = model_to_dict(product)
#         print(data)
#         return JsonResponse(data)


# #取得全部資料
# def get_all_product(request):
#     print("no2123123132")
#     data=Product.objects.all().values()
#     print(data)
#     final_data={}
#     for item in data :
#         final_data={ item['id']:item  for item in data }
#     print("connect success")
#     return JsonResponse(final_data)

#新增資料
# @csrf_exempt
# def add_product(reqeust):
#     json_data = json.loads(reqeust.body)
#     print(json_data)
#     try :
#         new_product=Product(**json_data)
#         new_product.save()
#         return JsonResponse({'status': 'POST success'})
#     except :
#         return JsonResponse({'error': 'Invalid JSON data'})

#刪除資料
# @csrf_exempt
# def delete_prodcut_by_id(request, product_id):
#     if request.method == 'DELETE':
#         try:
#             product = Product.objects.get(id=product_id)
#             product.delete()
#             return JsonResponse({'status': 'success'})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'no oooooooProduct not found'}, status=404)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
#
# #更新資料
# @csrf_exempt
# def product_update(request,id):
#     data=json.loads(request.body)
#     print(data)
#     print(data)
#     print("the id is ",id)
#     print(type(id))
#     if request.method == 'PUT':
#         try :
#             product = Product.objects.get(id=id)
#             print(product)
#             product.title=data["title"]
#             product.conttne=data['conttne']
#             product.price=data['price']
#             product.save()
#
#             return JsonResponse({'status': 'updata success'})
#         except :
#             return JsonResponse({'error': 'Invalid id '})
#     return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)
#
#
#
