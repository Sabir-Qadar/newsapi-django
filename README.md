# NewsWave

**Live demo:** [newsapi-django.onrender.com](https://newsapi-django.onrender.com/)

A Django-powered news portal that blends real-time headlines from the [NewsAPI.org](https://newsapi.org/) API with an admin-curated article system, wrapped in a custom Bootstrap 5 editorial frontend. Built to explore hybrid content architecture — mixing live third-party data with first-party, database-backed content in the same feed.

![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

NewsWave serves category-based news feeds (Business, Technology, Sports, Health, Entertainment, General) by combining two sources on every category page:

1. **Live articles** pulled in real time from NewsAPI's `top-headlines` endpoint.
2. **Admin-authored articles** stored in the local database via a custom `NewsArticle` model, so editorial staff can publish original or curated pieces alongside the live feed.

The two sets are merged and rendered through the same templates, so the reader sees one unified feed regardless of where a story came from.

## Features

- **Real-time headline aggregation** — category pages fetch fresh articles from NewsAPI's `top-headlines` endpoint (`country=us`, 12 articles per request) on every load.
- **Full-text search** — a dedicated search view queries NewsAPI's `everything` endpoint, sorted by publish date, for any keyword the user enters.
- **Hybrid article routing** — two separate detail views handle the two content sources:
  - API-sourced articles are rendered via `/article/` with their metadata (title, description, image, source URL, author, published date) passed straight through as query parameters, avoiding a second API round-trip per article.
  - Admin-authored articles are rendered via `/article/<slug>/`, looked up directly from the database using an auto-generated slug.
- **Django admin integration** — `NewsArticle` is fully registered in Django admin with list filters by category/date, search across title/description/content/author, and slug auto-population from the title.
- **Graceful API failure handling** — all outbound NewsAPI requests are wrapped in timeout + exception handling and fail safe to an empty list rather than crashing a page.
- **Custom error handling** — a branded 404 page for unmatched routes.
- **Static pages** — About and Contact pages for the publication.
- **Production-ready deployment** — WhiteNoise for static file serving, Gunicorn as the WSGI server, environment-variable-driven configuration (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `NEWS_API_KEY`) via `python-dotenv`, deployed live on Render.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| External data | [NewsAPI.org](https://newsapi.org/) (`top-headlines`, `everything`) via `requests` |
| Database | SQLite |
| Frontend | Bootstrap 5.3, vanilla JS, custom CSS |
| Static files | WhiteNoise |
| WSGI server | Gunicorn |
| Config | `python-dotenv` (environment-variable based settings) |
| Deployment | Render |

## Project Structure

```
newsapi-django/
├── build.sh                  # Render build step: install deps, collectstatic, migrate
├── requirements.txt
└── myproject/
    ├── manage.py
    ├── myproject/             # Django project config
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py / asgi.py
    ├── myapp/                 # Core application
    │   ├── models.py          # NewsArticle model
    │   ├── views.py           # home, category, article, article_detail, search, about, contact
    │   ├── services.py        # NewsAPI client functions (get_news, search_news)
    │   ├── admin.py           # Django admin config for NewsArticle
    │   ├── urls.py
    │   └── templates/pages/    # index, category, article, search, about, contact, 404
    └── static/
        ├── css/style.css
        └── images/logo.png
```

## Getting Started

### Prerequisites
- Python 3.10+
- A free API key from [newsapi.org](https://newsapi.org/)

### Setup

```bash
git clone https://github.com/Sabir-Qadar/newsapi-django.git
cd newsapi-django
pip install -r requirements.txt
```

Create a `.env` file inside `myproject/` with:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
NEWS_API_KEY=your-newsapi-org-key
```

Run migrations and start the server:

```bash
cd myproject
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### Deployment

The included `build.sh` runs the full production build step (dependency install, `collectstatic`, `migrate`) and is wired up for a one-click deploy on [Render](https://render.com/) using Gunicorn as the WSGI entry point.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Sabir Qadar**
[GitHub](https://github.com/Sabir-Qadar) · [Portfolio](https://sabir-qadar.github.io/Portfolio) · [LinkedIn](https://linkedin.com/in/sabir-qadar)
