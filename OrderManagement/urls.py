from django.urls import path
from .views import *

urlpatterns = [
    path('customers/add/',CustomersAdd),
    path('customers/',AllCustomers),
    path('customer/delete/<int:id>/',DeleteCustomers,name='Delete_customer'),
    path('customer/update/<int:id>/',UpdateCustomers,name='Update_customer'),

    path('add/orders/',OrdersAdd),
    path('orders/',OrdersList),
    path('delete/order/<int:id>/',OrdersDelete,name='Delete_order'),
    path('update/order/<int:id>/',OrdersUpdate,name='Update_order'),
]