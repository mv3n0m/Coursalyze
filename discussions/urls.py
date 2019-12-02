from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/<int:item_id>/',
         views.delete_item, name='delete_item'),
]
