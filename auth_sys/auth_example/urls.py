from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/register',views.register, name='register'),
]
