from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def category(request, name):
    return render(request, "pages/category.html", {"category": name.title()})

def article(request):
    return render(request, 'pages/article.html')

def search(request):
    return render(request, 'pages/search.html')