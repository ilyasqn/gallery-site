from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from photos.models import Category, Photo


# Create your views here.

class IndexView(ListView):
    template_name = 'photos/gallery.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('Category')
        if category is not None:
            context['photos'] = Photo.objects.filter(category__name=category)
        else:
            context['photos'] = Photo.objects.all()
        return context

class PhotoListView(TemplateView):
    template_name = 'photos/photo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_id = self.kwargs.get('pk')
        context['photo'] = Photo.objects.get(id=photo_id)
        return context
class AddPhotoView(ListView):
    template_name = 'photos/addPhoto.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.POST
        image = request.FILES.get('image')

        if 'category' in data and data['category'] != 'none':
            category = Category.objects.get(pk=data['category'])
        elif 'category_new' in data and data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            photo=image
        )
        return redirect('index')

