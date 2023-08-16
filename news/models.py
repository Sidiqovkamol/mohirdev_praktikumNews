from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView


class PublisherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)




class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Draft="DF", "Draft"
        Published="PB", "Published"


    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='news_picture/image')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time=models.DateTimeField(default=timezone.now)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2, choices=Status.choices,default=Status.Draft)

    objects=models.Manager()
    published=PublisherManager()

    class Meta:
        ordering=["-published_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("item_news_list", args=[self.slug])



class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=50)
    massage=models.TextField()

    def __str__(self):
        return self.email



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