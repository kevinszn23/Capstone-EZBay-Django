from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('listings/', views.ListingsList.as_view(), name="listings_list"),
    path('listings/new/', views.ListingsCreate.as_view(), name="listings_create"),
]