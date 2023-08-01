from django.urls import path
from . import views

urlpatterns = [
    path('wish_list/', views.view_wish_list, name='view_wish_list'),
    path('add_to_wish_list/<int:book_id>/', views.add_to_wish_list, name='add_to_wish_list'),
    path('remove_from_wish_list/<int:book_id>/', views.remove_from_wish_list, name='remove_from_wish_list'),
]
