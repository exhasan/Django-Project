from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),      # /properties/ shows the list
    path('add/', views.add_property, name='add_property'),  # /properties/add/ shows the form
 path('delete/<int:pk>/', views.delete_property, name='delete_property'),
 path('liked/', views.liked_properties, name='liked_properties'),
    path('register/', views.register, name='register'),  # Add this line
]