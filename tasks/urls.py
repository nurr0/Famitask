from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('api/tasks/', TaskList.as_view()),
    path('api/tasks/<int:pk>/', TaskDetail.as_view())
    # path('api/users_by_group/<int:pk>/', UsersByGroupListAPIView.as_view()),
    # path('api/group/<int:pk>/', GroupAPIView.as_view()),
    ]
