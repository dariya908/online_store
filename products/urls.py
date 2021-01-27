from django.urls import path
from .views import products_page,order_page, registrasia_page,user_page,aboutus_page

urlpatterns=[
    path('',products_page,name='products'),
    path('order/',order_page),
    path('registrasia/',registrasia_page,name='register'),
    path('user/',user_page),
    path('aboutus/',aboutus_page)
]