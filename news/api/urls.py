from django.urls import path

from . import views

urlpatterns = [
    path('auto-complete/', views.autocompleteAPIView.as_view(), name='auto-complete-api')
]