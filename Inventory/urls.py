from django.urls import path
from .views import *

urlpatterns = [
    path('products/add/',ProductsAdd),
    path('products/',AllProducts),
    path('products/delete/<int:id>/',DeleteProduct,name='Delete_product'),
    path('products/update/<int:id>/',UpdateProduct,name='Update_product'),
]