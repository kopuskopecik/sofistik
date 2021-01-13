from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='home'),
    path('kategoriler/<slug:slug>/', views.categories_detail, name='category'),
    path('tags/<slug:slug>/', views.tag_detail, name='tag'),
    path('<slug:slug>/', views.detail, name="detail"),
]