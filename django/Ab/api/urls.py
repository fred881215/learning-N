from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('auth', views.login),
    path('logout', views.logout),
    path('verification/send', views.send),
    # path('verification/check', views.check),
]