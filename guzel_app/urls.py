from django.urls import path
from . import views
urlpatterns = [
    path('getAllCat', views.getAllCat, name="getAllCat"),
    path('getAllProd', views.getAllProd, name="getAllProd"),
    path('getProdbyCat/<int:pk>/', views.getProdbyCat, name="getProdbyCat"),
    path('getprod/<int:pk>/', views.getprod, name="getprod"),
    path('login', views.login, name="login"),
    path('registration', views.register, name="registration"),
    path('createorder', views.createorder, name="createorder"),
    path('getorder/<int:pk>/', views.getorder, name="getorder"),
    path('getorderhistory', views.getorderhistory, name="getorderhistory"),
  ]