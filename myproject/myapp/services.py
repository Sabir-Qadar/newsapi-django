import requests
from django.conf import settings


def get_news(category="general"):

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "country": "us",
        "category": category,
        "pageSize": 12,
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("articles", [])

    except requests.RequestException:

        return []


def search_news(query):

    url = "https://newsapi.org/v2/everything"

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 20,
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("articles", [])

    except requests.RequestException:

        return []