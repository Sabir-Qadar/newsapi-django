import requests
from django.conf import settings


def get_news(category=None):
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "country": "us",
        "pageSize": 20,
    }

    if category:
        params["category"] = category

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])

    return []

def search_news(query):
    url = "https://newsapi.org/v2/everything"

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])

    return []


def get_article_by_url(article_url):
    url = "https://newsapi.org/v2/everything"

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "q": article_url,
        "language": "en",
        "pageSize": 1,
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        if articles:
            return articles[0]

    return None