from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Product2
from rest_framework.views import APIView


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products2 = Product2.objects.all()[0:4]
        serializer = ProductSerializer(products2, many=True)
        return Response(serializer.data)