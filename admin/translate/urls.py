from django.contrib import admin
from django.urls import path

from .views import MessageViewSet
urlpatterns = [
    path('message', MessageViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('message/<str:pk>', MessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]