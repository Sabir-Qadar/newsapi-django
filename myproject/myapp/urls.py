from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "category/<str:category_name>/",
        views.category,
        name="category"
    ),

    path("article/", views.article, name="article"),

    path(
        "article/<slug:slug>/",
        views.article_detail,
        name="article_detail"
    ),

    path("search/", views.search, name="search"),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),
]