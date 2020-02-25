from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game_detail'),
    path('guides/', views.GuideList.as_view(), name="guide_list"),
    path('guides/<int:pk>', views.GuideDetail.as_view(), name="guide_detail"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail")
]
