"""myblog URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import Index,Share,biancheng,suibi,biji,ganxiang
from . import views

urlpatterns = [   
    path('<int:page>/',Index.as_view(),name='index'),
    path('share/',Share.as_view(),name='share'),
    path('info/<int:blog_id>',views.info,name='info'),
    path('search/',views.get_search,name='search'),
    path('biancheng/',biancheng.as_view(),name='biancheng'),
    path('suibi/',suibi.as_view(),name='suibi'),
    path('biji/',biji.as_view(),name='biji'),
    path('ganxiang/',ganxiang.as_view(),name='ganxiang'),
    path('about/',views.about,name='about'), 

]
