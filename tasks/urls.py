from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('api/tasks/<int:group_id>/', TaskList.as_view()),
    path('api/tasks_detail/<int:pk>/', TaskDetail.as_view()),
    path('api/subtasks/<int:parent_task_id>/', SubtaskList.as_view()),
    path('api/subtasks_detail/<int:pk>/', SubtaskDetail.as_view()),
    path('api/tasks/<int:task_id>/responsible/',
          ResponsibleOnTaskList.as_view()),
    path('api/tasks/set_responsible/',
         ResponsibleOnTaskCreate.as_view()),
    path('api/tasks/remove_responsible/<int:pk>/',
         ResponsibleOnTaskDelete.as_view()),
    ]
