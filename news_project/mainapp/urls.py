"""news_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('news/<int:pk>/', mainapp.select_news, name='select_news'),

    path('comment', mainapp.comments, name='comment'),
    path('comment/add/', mainapp.create_comments, name='create_comments'),
    path('comment/remove/<int:pk>', mainapp.remove_comments, name='remove_comments'),
    path('comment/edit/<int:pk>', mainapp.update_comments, name='update_comments'),
    path('about/', mainapp.about, name='about'),
    path('favorite/', mainapp.favorite, name='favorite'),
    path('favorite/remove/<int:pk>/', mainapp.remove_favorite, name='remove_favorite'),
    path('favorite/add/<int:pk>/', mainapp.add_favorite, name='add_favorite'),
]
