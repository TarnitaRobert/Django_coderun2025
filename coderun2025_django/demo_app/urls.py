from django.urls import path 
from . import views

app_name = 'demo_app'
urlpatterns = [
    path('', views.demo_app_page, name = 'demo_page')
]
