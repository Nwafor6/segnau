from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import (BlogPost, ContactDb, JoinDb)
from .forms import *
# Create your views here.

class HomePage(TemplateView):
	template_name ='mainapp/home.html'
class AboutPage(TemplateView):
	template_name ='mainapp/about.html'

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
@login_required
def DatabaseView(request):
	joindb=JoinDb.objects.all()
	contactdb=ContactDb.objects.all()
	return render(request, 'mainapp/database.html', {'joindb':joindb,"contactdb":contactdb})

@login_required
def DatabaseDetailView(request, pk):
	joindb=JoinDb.objects.get(pk=pk)
	return render(request, 'mainapp/databaseview.html', {'joindb':joindb})
@login_required
def DatabaseDetailView_2(request, pk):
	contactdb=ContactDb.objects.get(pk=pk)
	return render(request, 'mainapp/databaseview.html', {"contactdb":contactdb}) 	

def BlogPostListView(request):
	posts=BlogPost.objects.all()
	return render(request, 'mainapp/blog.html', {"posts":posts}) 
def BlogPosDetailView(request, slug):
	post=BlogPost.objects.get(slug=slug)
	return render(request, 'mainapp/blogdetail.html', {"post":post}) 	

def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)