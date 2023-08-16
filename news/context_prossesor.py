
from .models import News,Category


def leastNews(request):
    least_news=News.published.all().order_by("-published_time")[:10]
    categories=Category.objects.all()
    context ={
        'least_news':least_news,
        'categories':categories,

    }
    return context

