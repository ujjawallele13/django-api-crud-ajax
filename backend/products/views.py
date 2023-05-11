from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from . import serializers

# Create your views here.

@api_view(['POST', 'PUT', 'DELETE', 'GET'])
def products(request, id=None):
    if request.method == 'GET':
            if id is None:
                products = Product.objects.all()
                products = serializers.ProductSerializer(products,many=True).data
                return Response(data=products,status=status.HTTP_200_OK)
            else :
                try: 
                    product = Product.objects.get(product_id = id) 
                except Product.DoesNotExist: 
                    return Response({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
                products = serializers.ProductSerializer(product).data
                return Response(data=products,status=status.HTTP_200_OK)
            
    if request.method == 'POST':
        data = request.data.copy()  
        data.pop('product_id', None)
        serializer = serializers.ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Missing one or more required fields.'}, status=status.HTTP_400_BAD_REQUEST)
       
    if request.method == 'DELETE':
        try: 
            product = Product.objects.get(product_id = id) 
        except Product.DoesNotExist: 
            return Response({'message': 'The product to be deleted does not exist'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'message': 'product deleted'},status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        try: 
            product = Product.objects.get(product_id = id) 
        except Product.DoesNotExist: 
            return Response({'message': 'The product to be updated does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Missing one or more required fields.'},status=status.HTTP_400_BAD_REQUEST)
         

