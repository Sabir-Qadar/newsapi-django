from django.shortcuts import render
from .models import NewsArticle
from .services import get_news, search_news

def home(request):
    api_articles = get_news("general")

    admin_articles = NewsArticle.objects.all().order_by("-created_at")

    formatted_admin_articles = []

    for article in admin_articles:
        formatted_admin_articles.append({
            "title": article.title,
            "description": article.description,
            "content": article.content,
            "urlToImage": article.image_url,
            "author": article.author,
            "category": article.category,
            "url": article.article_url,
            "publishedAt": article.published_at.isoformat() if article.published_at else "",
        })

    articles = formatted_admin_articles + api_articles

    return render(
        request,
        "pages/index.html",
        {
            "articles": articles
        }
    )

def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def category(request, category_name):
    api_articles = get_news(category_name)

    admin_articles = NewsArticle.objects.filter(
        category=category_name
    ).order_by("-created_at")

    formatted_admin_articles = []

    for article in admin_articles:
        formatted_admin_articles.append({
            "title": article.title,
            "description": article.description,
            "content": article.content,
            "urlToImage": article.image_url,
            "author": article.author,
            "category": article.category,
            "url": article.article_url,
            "publishedAt": (
                article.published_at.isoformat()
                if article.published_at
                else ""
            ),
        })

    articles = formatted_admin_articles + api_articles

    return render(
        request,
        "pages/category.html",
        {
            "category": category_name.title(),
            "articles": articles,
        }
    )

def article(request, slug=None):
    if slug:
        article_data = NewsArticle.objects.filter(slug=slug).first()

        if article_data:
            return render(
                request,
                "pages/article.html",
                {
                    "article": {
                        "title": article_data.title,
                        "description": article_data.description,
                        "content": article_data.content,
                        "urlToImage": article_data.image_url,
                        "author": article_data.author,
                        "publishedAt": (
                            article_data.published_at.isoformat()
                            if article_data.published_at
                            else ""
                        ),
                        "url": article_data.article_url,
                    }
                }
            )

    return render(
        request,
        "pages/article.html",
        {
            "article": None
        }
    )

def search(request):
    query = request.GET.get("q", "").strip()

    articles = []

    if query:
        articles = search_news(query)

    return render(
        request,
        "pages/search.html",
        {
            "articles": articles,
            "query": query,
        }
    )


def custom_404(request, exception):
    return render(request, "pages/404.html", status=404)