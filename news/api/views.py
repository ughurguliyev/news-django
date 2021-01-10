from django.shortcuts import render
from django.urls import reverse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import autocompleteSerializer
from core.models import Post

# Create your views here.

class autocompleteAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = autocompleteSerializer

    def get_queryset(self):
        data = self.request.query_params
        if data.get('s'):
            kw = data.get('s')
            queryset = Post.objects.filter(title__icontains=kw)  
        else:
            queryset = Post.objects.all()

        return queryset