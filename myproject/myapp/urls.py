from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),path("category/<str:name>/", views.category, name="category"),path('article/', views.article, name='article'),
    path('search/', views.search, name='search'),
]