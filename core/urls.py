from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('api/group/', GroupListCreateView.as_view()),
    path('api/group/<int:pk>/', GroupDetailView.as_view()),
    path('api/user_group_relation/<int:group_id>/users/',
         UserGroupRelationList.as_view()),
    path('api/user_group_relation/<int:pk>/',
         UserGroupRelationDetail.as_view()),
    path('api/user_group_relation/create/', UserGroupRelationCreate.as_view()),

]
