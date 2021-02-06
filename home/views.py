from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from personalaccount.models import RequestChange, News
from .serializers import RequestAPI


def home(request):
    last_news = News.objects.filter(news_is_publish=True).latest('pk')
    context = {
        'last_news': last_news,
    }
    return render(request, 'home/content/index.html', context)


def support(request):
    return render(request, 'home/content/support.html')


def news(request):
    list_news = News.objects.filter(news_is_publish=True)
    context = {
        'list_news': list_news,
    }
    return render(request, 'home/content/news.html', context)


def newsview(request, pk):
    list_news = News.objects.filter(news_is_publish=True)
    news_view = None
    next_news = None
    cnt = 0
    flag = False
    for item in list_news:
        if not flag:
            if item.pk == pk:
                news_view = item
                flag = True
            cnt += 1
        else:
            next_news = item
            break
    context = {
        'news_view': news_view,
        'next_news': next_news,
        'list_news': list_news,
    }
    return render(request, 'home/content/newsview.html', context)


# api
class RequestList(APIView):
    """Список заявок"""
    def get(self, request):
        req = RequestChange.objects.all()
        s = RequestAPI(req, many=True)
        return Response(s.data)
