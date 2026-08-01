from django.db import models
from django.utils.text import slugify


class NewsArticle(models.Model):

    CATEGORY_CHOICES = [
        ("business", "Business"),
        ("technology", "Technology"),
        ("sports", "Sports"),
        ("health", "Health"),
        ("entertainment", "Entertainment"),
        ("general", "General"),
    ]

    title = models.CharField(max_length=300)

    description = models.TextField(blank=True)

    content = models.TextField(blank=True)

    image_url = models.URLField(blank=True)

    author = models.CharField(max_length=200, blank=True)

    slug = models.SlugField(
        max_length=300,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general"
    )

    article_url = models.URLField(blank=True)

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title