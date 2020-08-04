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
    path('blood/pressure', views.blood_pressure),
    path('weight', views.body_weight),
    path('blood/sugar', views.blood_sugar),
    path('last_upload', views.last_upload),
    path('records', views.records),
    path('diary', views.diary_list),
    path('diet', views.diary_diet),
    path('delete', views.diary_records_delete),
    path('care', views.care),
]

