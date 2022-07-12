from django.urls import path
from . import views
from .views import (HomePage,AboutPage,
ContactPage,JoinPage
	)

urlpatterns=[
	path ('', HomePage.as_view(), name="home"),
	path ('about', AboutPage.as_view(), name="about"),
	path ('blog', views.BlogPostListView, name="blog"),
	path ('join-us', JoinPage.as_view(), name="join"),
	path ('contact-us', ContactPage.as_view(), name="contact"),
	path ('database', views.DatabaseView, name="database"),
	path ('database/join-us/<str:pk>/', views.DatabaseDetailView, name="database"),
	path ('database/contact-us/<str:pk>/', views.DatabaseDetailView_2, name="database1"),
	path ('blog/<slug:slug>/', views.BlogPosDetailView, name="blogdetail"),
]