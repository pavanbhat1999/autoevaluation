from django.urls import path

from input import views

urlpatterns = [
    path('', views.input, name='input'),
   # path('result/', views.predict)
]