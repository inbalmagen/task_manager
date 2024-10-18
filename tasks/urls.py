from django.urls import path
from .views import task_list
from tasks import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
]