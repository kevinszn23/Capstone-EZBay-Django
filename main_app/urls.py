from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('listings/', views.ListingsList.as_view(), name="listings_list"),
    path('listings/new/', views.ListingsCreate.as_view(), name="listings_create"),
    path('listings/<int:pk>/', views.ListingsDetail.as_view(), name="listings_detail"),
    path('listings/<int:pk>/update',views.ListingsUpdate.as_view(), name="listings_update"),
    path('listings/<int:pk>/delete',views.ListingsDelete.as_view(), name="listings_delete"),
]