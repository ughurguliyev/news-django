from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from .models import Post, Contact, Comment, Category
from .forms import ContactForm, CommentForm
from .actions import ContactCreation


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'



class TestPage(TemplateView):
    template_name = 'pages/test.html'


class ContactPageView(FormView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'pages/contact.html'


    def form_valid(self, form):
        result = ContactCreation().create(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'), 
            subject=form.cleaned_data.get('subject'), 
            message=form.cleaned_data.get('message')  
        )
        return HttpResponseRedirect(self.get_success_url())


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class CategoryPageView(ListView):
    template_name = 'pages/categori.html'
    model = Category
    context_object_name = 'categories'


class CategoryListPageView(DetailView):
    template_name = 'pages/categori.html'
    model = Category

    def get_category_name(self):
        return self.get_object().name

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cat_name = self.get_category_name()
        context['category_articles'] = Post.objects.filter(categories__name=cat_name)
        return context


class LatestNewsPageView(TemplateView):
    template_name = 'pages/latest_news.html'


class ArticleDetailView(FormView, DetailView):
    model = Post
    context_object_name = 'article'
    template_name = 'pages/article-detail.html'
    form_class = CommentForm
    success_url = '/'

    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count += 1
        obj.save()

        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        obj = self.get_object()
        new_comment = Comment.objects.create(
            body = form.cleaned_data.get('comment'),
            email = form.cleaned_data.get('email'),
            commenter = form.cleaned_data.get('name'),
            website = form.cleaned_data.get('website')
        )
        new_comment.save()
        obj.comments.add(new_comment)

        return super().form_valid(form)
    
    def get_post_numbers_in_categories(self):
        obj = Category.objects.all()
        category_names = [cat.name for cat in obj]
        number_list = []
        for name in category_names:
            number_list.append(f'{name} ({len(Post.objects.filter(categories__name=name))})')   
        return number_list

    def get_next_post(self):
        obj = self.get_object()
        pk = obj.pk
        next_post = Post.objects.filter(id=pk+1)
        return next_post

    def get_prev_post(self):
        obj = self.get_object()
        pk = obj.pk
        prev_post = Post.objects.filter(id=pk-1)
        return prev_post

    def get_comments(self):
        obj = self.get_object()
        return obj.comments.all()

    def get_recent_posts(self):
        obj = Post.objects.all().order_by('-created_at')[:4]
        return obj

    def get_categories(self):
        obj = self.get_object()
        return obj.categories.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'article': self.get_object(),
            'categories': self.get_categories(),
            'all_categories': self.get_post_numbers_in_categories(),
            'comments': self.get_comments(),
            'recent_posts': self.get_recent_posts(),
            'next_post': self.get_next_post(),
            'previous_post': self.get_prev_post()
        }

        return context


    
        