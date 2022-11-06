from django.shortcuts import render

from core.models import History, Chapter, News, Image


def index(request):
    image = Image.objects.get(name="Krieg War")
    news = News.objects.all()
    context = {
        "phrase": "News",
        "news": news,
        "krieg": image,
    }

    return render(request, 'app/pages/index.html', context=context)


def history(request):
    histories = History.objects.select_related("image")
    context = {
        "phrase": "History",
        "histories": histories,
    }

    return render(request, 'app/pages/history.html', context=context)


def chapter(request):
    chapters = Chapter.objects.select_related("image")
    context = {
        "phrase": "Chapter",
        "chapters": chapters
    }

    return render(request, 'app/pages/chapter.html', context=context)


def login(request):
    image = Image.objects.get(name="Login Image")
    context = {
        "phrase": "Login",
        "LoginImage": image
    }

    return render(request, 'app/pages/login.html', context=context)


def register(request):
    image = Image.objects.get(name="Register Image")
    context = {
        "phrase": "Resgiter",
        "RegisterImage": image
    }

    return render(request, 'app/pages/register.html', context=context)


