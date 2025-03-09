"""
URL configuration for django42Cart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog/<str:cat>', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('catalog/buy/<str:cat>/<int:itemid>',views.buy, name='buy'),
    path('catt/delete/<int:itemid>', views.delete, name='delete'),
    path('cart/edit/<int:itemid>/<str:num>', views.edit, name='edit'),

]
