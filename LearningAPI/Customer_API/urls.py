from django.urls import path
from Customer_API import views

urlpatterns = [
    path('api/customer/', views.CustomerListAPIView.as_view(), name="customers-api"), 
    path('api/customer/<int:id>', views.CustomerDetailAPIView.as_view(), name="customer-api"),

]