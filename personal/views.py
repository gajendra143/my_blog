from django.shortcuts import render
from .models import BlogTable
from django.views.generic import DetailView


def homeview(request):
    return render(request, 'homepage.html')


def contactview(request):
    return render(request, 'contact.html')


def blogview(request):
    data = BlogTable.objects.all()
    return render(request, 'blogpage.html', {'data': data})


class PostView(DetailView):
    model = BlogTable
    template_name = 'postpage.html'
