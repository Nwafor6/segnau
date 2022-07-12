from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import (BlogPost, ContactDb, JoinDb)
from .forms import *
# Create your views here.

class HomePage(TemplateView):
	template_name ='mainapp/home.html'
class AboutPage(TemplateView):
	template_name ='mainapp/about.html'


class BlogPage(CreateView):
	model=BlogPost
	form_class = BlogForm
	template_name ='mainapp/blog.html'
	success_url ='blog'
class JoinPage(CreateView):
	model=JoinDb
	form_class = JoinForm
	success_url ='join-us'
	template_name ='mainapp/join.html'
class ContactPage(CreateView):
	model=ContactDb
	form_class = ContactForm
	success_url ='contact-us'
	template_name ='mainapp/contact.html'

def DatabaseView(request):
	joindb=JoinDb.objects.all()
	contactdb=ContactDb.objects.all()
	return render(request, 'mainapp/database.html', {'joindb':joindb,"contactdb":contactdb})

def DatabaseDetailView(request, pk):
	joindb=JoinDb.objects.get(pk=pk)
	return render(request, 'mainapp/databaseview.html', {'joindb':joindb})

def DatabaseDetailView_2(request, pk):
	contactdb=ContactDb.objects.get(pk=pk)
	return render(request, 'mainapp/databaseview.html', {"contactdb":contactdb}) 	

def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)