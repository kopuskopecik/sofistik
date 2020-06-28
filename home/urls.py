from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.detail, name="detail"),
]