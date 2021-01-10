from .models import Post 

from datetime import datetime, timedelta

def recent_articles(request):
    news = Post.objects.all().order_by('-created_at')[:7]
    return {'recent_articles': news}

def trending_articles(request):
    news = Post.objects.all().order_by('-created_at')
    news_top = news.first()
    news_bottom = news[1:4]
    news_right = news[4:10]
    trending_now_news = Post.objects.filter(trending_now=True)

    return {
        'trending_article_top': news_top,
        'trending_articles_bottom': news_bottom,
        'trending_articles_right': news_right,
        'trending_now_articles': trending_now_news
    }


def weekly_top_news(request):
    news = Post.objects.filter(created_at__gte=datetime.now()-timedelta(days=7)).order_by('-view_count')
    first_weekly_news = news[:4]
    second_weekly_news = news[4:10]

    return {
        'first_weekly_news': first_weekly_news,
        'second_weekly_news': second_weekly_news
    }
