from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "published_at",
        "created_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "content",
        "author",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-created_at",
    )