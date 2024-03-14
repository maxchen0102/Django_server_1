from django.shortcuts import render
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from django.forms.models import model_to_dict
# Create your views here.


# def api_home(request): 
    
#     try :
#         params = request.GET.dict()
#         print(params)
#         print("connect success")
        
#     except:
#         pass
#     print(request.POST)
#     print(request.GET)

    
   
#     return  JsonResponse({"status": "GET success"})

# @csrf_exempt
# def api_post(request):
#     if request.method == 'POST':
#         # Handle POST request with JSON data
#         try:
#             json_data = json.loads(request.body)
#             # Process JSON data here
#             print(json_data)
#             return JsonResponse({'status': 'POST success'})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     else:
#         # Handle other HTTP methods (e.g., GET)
#         return JsonResponse({'error': 'Unsupported method'}, status=405)
    
#取得資料by id


def test(request):
    data={"status":"ok"}
    return JsonResponse(data)
def get_product(request,id):
    print("this")
    if id :
        product=Product.objects.get(id=id)
        data = model_to_dict(product)
        print(data)
        return JsonResponse(data)

#取得全部資料
def get_all_product(request):
    print("no2123123132")
    data=Product.objects.all().values()
    print(data)
    final_data={}
    for item in data :
        final_data={ item['id']:item  for item in data }
    print("connect success")
    return JsonResponse(final_data)

#新增資料
@csrf_exempt
def add_product(reqeust): 
    json_data = json.loads(reqeust.body)
    print(json_data)
    try : 
        new_product=Product(**json_data)
        new_product.save()
        return JsonResponse({'status': 'POST success'})
    except : 
        return JsonResponse({'error': 'Invalid JSON data'})

#刪除資料
@csrf_exempt
def delete_prodcut_by_id(request, product_id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'status': 'success'})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'no oooooooProduct not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
#更新資料
@csrf_exempt
def product_update(request,id):
    data=json.loads(request.body)
    print(data)
    print(data)
    print("the id is ",id)
    print(type(id))
    if request.method == 'PUT':
        try : 
            product = Product.objects.get(id=id)
            print(product)
            product.title=data["title"]
            product.conttne=data['conttne']
            product.price=data['price']
            product.save()
            
            return JsonResponse({'status': 'updata success'})
        except : 
            return JsonResponse({'error': 'Invalid id '})
    return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)