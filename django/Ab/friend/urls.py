"""puyuanAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('code', views.friend_code),
    path('list', views.friend_list),
    path('requests', views.friend_requests),
    path('send', views.friend_send),
    path('<int:friend_uid>/accept', views.friend_accept),
    path('<int:friend_uid>/refuse', views.friend_refuse),
    path('<int:friend_uid>/remove', views.friend_delete),
    path('results', views.friend_results),
    path('remove', views.friend_remove),
]

