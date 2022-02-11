from typing import Generic
from django.shortcuts import render
from rest_framework. mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from mixins.models import ProductsModel
from mixins.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class ProdPagination(LimitOffsetPagination):
#     page_size = 3
#     # age_size_query_param = 'page_size'
#     # max_page_size = 2

class ProductViewset(viewsets.ModelViewSet): #insted of ModelViewSet we can use ReadonlyModelViewSet - this will remove add, edit and delete option
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = ProdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price']


'''

class ProductList(ListAPIView,CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer


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
