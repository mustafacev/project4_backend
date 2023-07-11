from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('house/', views.HouseList.as_view(), name="house_list"),
    path('house/new/', views.HouseCreate.as_view(), name="house_create"),
    path('house/<int:pk>/', views.HouseDetail.as_view(), name="house_detail"),
    path('house/<int:pk>/update',views.HouseUpdate.as_view(), name="house_update"),
    path('house/<int:pk>/delete',views.HouseDelete.as_view(), name="house_delete"),
    path('house/<int:pk>/realestate/new/', views.RealestateCreate.as_view(), name="realestate_create")
]