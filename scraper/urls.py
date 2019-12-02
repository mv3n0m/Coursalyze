from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.new_search),
    path('details/<slug>/', views.detail),
    path('update/', views.update, name="update"),
]
