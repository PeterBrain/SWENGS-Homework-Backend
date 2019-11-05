from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.department_list),
    path('department/<int:pk>/', views.department_detail),
]