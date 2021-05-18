from django.urls import path
from DemoAPI import views

# account : phanthetue
# pass : Mitcute0105
urlpatterns = [
   # api riêng cho từng cái 
    path('customer/', views.CustomerListAPIView.as_view(), name="customers-api"), 
    path('customer/<int:id>', views.CustomerDetailAPIView.as_view(), name="customer-api"),
]