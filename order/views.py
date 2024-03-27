#import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from .models import Order, OrderItem
from .serializers import OrderSerializer,OrderItemSerializer


@api_view(['POST'])
def checkout(request):
    payload = request.data
    items_data = payload.pop('items', [])  # Get items data or an empty list if not provided
    totalPrice = payload['totalPrice']
    serializer = OrderSerializer(data=payload)

    if serializer.is_valid():
        try:

            order_instance = serializer.save(total_price=totalPrice)


            for item_data in items_data:
                product_instance = Product.objects.get(id=str(item_data['product']))
                save_data = {
                    'order': order_instance,
                    'product': product_instance,
                    'quantity': item_data['quantity'],
                    'price': item_data['price']
                }
                item_serializer = OrderItemSerializer(data=save_data)
                if item_serializer.is_valid():
                    try:
                        orderItem2 = OrderItem.objects.create(**save_data)
                        return Response({'message': 'Order'})
                    except Exception as e:
                        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                return Response({'message': 'Order'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Return validation errors if Order creation fails
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrdersList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

