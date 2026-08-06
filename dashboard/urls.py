from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('add-program/', views.add_program, name='add_program'),

    path('edit-program/<int:id>/', views.edit_program, name='edit_program'),

    path('delete-program/<int:id>/', views.delete_program, name='delete_program'),
]