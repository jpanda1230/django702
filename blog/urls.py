"""hellomeltingpod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/comments/new/', views.comment_new, name='comment_new'),
    #path('<int:post_pk>/comments/(?P<pk>\d+)/edit/', views.comment_edit, name='comment_edit')
    path('<int:post_pk>/comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('<int:post_pk>/comments/<int:pk>/delete/', views.comment_delete, name='comment_delete')

]