from django.contrib import admin
from django.urls import path, include
from .views import (
    ShopListApiView,
    ShopDetailApiView
)


urlpatterns = [
    path('api', ShopListApiView.as_view()),
    path('api/<int:shop_id>/', ShopDetailApiView.as_view()),
]