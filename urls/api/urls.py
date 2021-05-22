from django.urls import path

from urls.api import views

urlpatterns = [
    path('', views.input, name='input'),
   # path('results/', views.results,name="results")
]