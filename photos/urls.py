from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('photo/<str:pk>/', views.PhotoListView.as_view(), name='photo'),
    path('add/', views.AddPhotoView.as_view(), name='add'),
]