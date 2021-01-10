from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('contact-us/', views.ContactPageView.as_view(), name='contact-page'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path('category/', views.CategoryPageView.as_view(), name='category-page'),
    path('category/<slug>', views.CategoryListPageView.as_view(), name='category-list-page'),
    path('latest-news', views.LatestNewsPageView.as_view(), name='latest-news-page'),
    path('article/<slug>/', views.ArticleDetailView.as_view(), name='article-detail-page'),
    path('test', views.TestPage.as_view())
]