from django.urls import path
from . import views
from .views import student_api

urlpatterns = [
  path('api/students/', views.student_api, name='student_api'),
  path('api/departments/', views.department_api, name='department_api'),
]