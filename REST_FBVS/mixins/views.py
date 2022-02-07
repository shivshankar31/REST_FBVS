from typing import Generic
from django.shortcuts import render
from rest_framework. mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from mixins.models import ProductsModel
from mixins.serializers import ProductSerializer
# Create your views here.


class ProductList(ListAPIView,CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

'''
class ProductList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class ProductDetail(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)

'''
