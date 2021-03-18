from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name="api_overview"),

    path('task-list/', views.task_list, name="task_list"),
    path('task-create/', views.task_create, name="task_create"),

    path('task-detail/<int:task_pk>/', views.task_detail, name="task_detail"),
    path('task-update/<int:task_pk>/', views.task_update, name="task_update"),
    path('task-delete/<int:task_pk>/', views.task_delete, name="task_delete"),
]