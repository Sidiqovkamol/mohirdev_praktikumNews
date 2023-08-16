from .views import  New_detail, HomePageView, ContactPageView,\
    LocalNewsView,ForeignNewsView,SportNewsView,TechnoNewsView

from django.urls import path

urlpatterns = [
    path('',HomePageView.as_view(), name='home_page_view'),
    path("news/<slug:news>/",New_detail,name='item_news_list'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page_us'),
    path('foreign/',ForeignNewsView.as_view(), name='foreign_page_view'),
    path("sport/", SportNewsView.as_view(), name="sport_page_view"),
    path("local/",LocalNewsView.as_view(),name='local_page_view'),
    path("texnology/", TechnoNewsView.as_view(),name="techno_page_view"),
]

