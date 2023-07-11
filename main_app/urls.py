from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('house/', views.HouseList.as_view(), name="house_list"),
    path('house/new/', views.HouseCreate.as_view(), name="house_create"),
    path('house/<int:pk>/', views.HouseDetail.as_view(), name="house_detail"),
]