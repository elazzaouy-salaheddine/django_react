from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('test01',views.index),
    path('test02',views.index),
]