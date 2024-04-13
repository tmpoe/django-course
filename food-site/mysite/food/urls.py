from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.item, name='item'),
    path('add', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item')
]
