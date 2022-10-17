from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Shop
from .serializers import ShopSerializer


class ShopListApiView(APIView):
    def get(self, request, *args, **kargs):
        # List all the parameters #
        todos = Shop.objects.all()
        serializer = ShopSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kargs):
        # Create parameter with given data #
        data = {
            'name': request.data.get('name'),
            'value': request.data.get('value'),
            'isSecret': request.data.get('isSecret')
        }
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ShopDetailApiView(APIView):
    def get_object(self, shop_id):
        try:
            return Shop.objects.get(id=shop_id)
        except Shop.DoesNotExist:
            return None

    def get(self, request, shop_id, *args, **kargs):
        # Get a parameter with given id #
        parameter = self.get_object(shop_id)
        if not parameter:
            return Response({
                "res": "Object with parameter name does not exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = ShopSerializer(parameter)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, shop_id, *args, **kargs):
        # Update parameter with given id #
        parameter = self.get_object(shop_id)
        if not parameter:
            return Response({
                "res": "Object with parameter name does not exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
            'value': request.data.get('value'),
            'isSecret': request.data.get('isSecret')
        }
        serializer = ShopSerializer(instance=parameter, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shop_id, *args, **kargs):
        # Remove parameter with given id #
        parameter = self.get_object(shop_id)
        if not parameter:
            return Response({
                "res": "Object with parameter name does not exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        parameter.delete()
        return Response({
            "res": "Object deleted!"
        }, status=status.HTTP_200_OK)