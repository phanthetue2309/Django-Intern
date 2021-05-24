"""ShopWeb_Building_Material URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Users import views as user_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi  # class drf_yasg to show full view of api
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="BUILDING MATERIALS",
        default_version='v1',
        description="Test API",
        terms_of_service="",
        contact=openapi.Contact(email="love01052309@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    # permission_classes=(permissions.IsAdminUser,),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebShop.urls')),
    path('product/', include('Product.urls')),
    path('warehouse/', include('Warehouse.urls')),
    path('people/', include('People.urls')),
    path('bill/', include('Bill.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='Users/password_reset_complete.html'), name='password_reset_complete'),

    # show all API 
    path('api/', schema_view.with_ui('swagger',
                                     cache_timeout=0), name='schema-swagger-ui'),

    path('api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]
