from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('cross_off/<str:pk>/', views.cross_off, name="cross_off"),
    path('uncross/<str:pk>/', views.uncross, name="uncross"),
]