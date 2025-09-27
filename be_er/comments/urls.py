from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment-list'),
    path('<int:id>/', views.comment_detail, name='comment-detail'),
]
