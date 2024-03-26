from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Product2 , Category
from rest_framework.views import APIView
from django.http import Http404

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products2 = Product2.objects.all()[0:4]
        serializer = ProductSerializer(products2, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product2.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product2.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)