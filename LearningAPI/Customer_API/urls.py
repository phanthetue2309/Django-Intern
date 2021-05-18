from django.urls import path
from Customer_API import views

urlpatterns = [
    path('', views.CustomerListAPIView.as_view(), name="customers-api"), 
    path('<int:id>', views.CustomerDetailAPIView.as_view(), name="customer-api"),

]