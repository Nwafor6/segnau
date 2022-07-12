from django.contrib import admin
from .models import BlogPost
# Register your models here.
class AdminBlogPost(admin.ModelAdmin):
	list_display= ['title', 'slug','pub_on']
	prepopulated_fields= {'slug': ('title',)}

admin.site.register(BlogPost, AdminBlogPost)