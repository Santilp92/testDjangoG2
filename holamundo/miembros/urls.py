from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.newMembers, name='addMember'),
    path('get', views.getMembers, name='getMembers'),
]
