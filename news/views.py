from django.http import Http404, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import ContactsForm
from .models import News,Category
# Create your views here.


# def New_list(request):
#     news_list=News.published.all()
#     context= {
#         'news_list':news_list
#     }
#
#     return render(request,'news/news_list.html',context)


def New_detail(request, news):
    news=get_object_or_404(News,slug=news, status=News.Status.Published)
    context= {
        'news':news
    }

    return render(request, 'news/news_detail.html', context)





# # 1-usl funksiya orqali
# def HomePageView(request):
#     categories=Category.objects.all()
#     news_list=News.published.all().order_by('-published_time')[:10]
#     local_one=News.published.filter(category__name="Mahalliy").order_by("-published_time")[0]
#     local_news=News.published.all().filter(category__name="Mahalliy").order_by("-published_time")[1:5]
#     context={
#         'news_list':news_list,
#         'categories':categories,
#         'local_one':local_one,
#         'local_news':local_news
#     }
#     return render(request, 'news/home.html', context)


# 2-usul class orqali
class HomePageView(ListView):
    model = News
    template_name = "news/home.html"
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all()
        context["news_list"]=News.published.all().order_by('-published_time')[:4]
        # context["local_one"]=News.published.filter(category__name="Mahalliy").order_by("-published_time")[0]
        context["local_news"]=News.published.all().filter(category__name="Mahalliy").order_by("-published_time")[:5]
        context["xorij_xabarlari"]=News.published.all().filter(category__name="Xorijiy").order_by("-published_time")[:5]
        context["sport_xabarlari"]=News.published.all().filter(category__name="Sport").order_by("-published_time")[:5]
        context["texnologiya_xabarlar"]=News.published.all().filter(category__name="Texnologiya").order_by("-published_time")[:5]

        return context



# def ContactPageView(request):
#     print(request.POST)
#     form=ContactsForm(request.POST)
#     if request.method=="POST" and form.is_valid():
#         form.save()
#         return HttpResponse("Biz bilan bo'glangazi uchun rahmat!")
#
#     context={
#         'form':form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form=ContactsForm()
        context={
            "form":form
        }
        return render(request, "news/contact.html", context)

    def post(self, request):
        form=ContactsForm(request.POST)
        if request.method=="POST" and form.is_valid():
            form.save()
            return HttpResponse("Biz bilan bog'langaniz uchun rahmat!")

        context={
            "form":form
        }
        return render(request, "news/contact.html", context)



class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name ="mahalliy_yangiliklar"

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="Mahalliy")
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = "sport_yangiliklar"

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="Sport")
        return news


class TechnoNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name ="texnologiya_yangiliklar"

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="Texnologiya")
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/dunyo.html'
    context_object_name ="dunyo_yangiliklar"

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="Xorijiy")
        return news

