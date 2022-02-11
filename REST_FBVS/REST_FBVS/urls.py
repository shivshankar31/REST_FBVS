"""REST_FBVS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from fbvapp.views import student_detail,student_list
from cbvapp.views import EmployeesDetails, EmployeeList
# from mixins.views import ProductDetail, ProductList
from rest_framework.routers import DefaultRouter
from mixins import views
from nsapp.views import AuthorDetailView, AuthorListView, BookDetailView, BookListView

router = DefaultRouter()
router.register('product', views.ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_list),
    path('students/<int:pk>', student_detail),
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeesDetails.as_view()),
    # path('products/', ProductList.as_view()),
    # path('products/<int:pk>', ProductDetail.as_view()),
    path('', include(router.urls)),
    path('author',AuthorListView.as_view()),
    path('author/<int:pk>',AuthorDetailView.as_view()),
    path('book',BookListView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
]

