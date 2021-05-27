from django.urls import path

from urls.odu_api import views

urlpatterns = [
    path('', views.get_answers, name='get_answers'),
    path('calculateresults',views.get_results,name="get_results"),
    path('show_results',views.show_results,name="show_results"),
]