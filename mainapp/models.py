from django.db import models
from django.utils.text import slugify
# Create your models here.
class BlogPost(models.Model):
	title=models.CharField(max_length=200)
	slug=models.SlugField()
	body=models.TextField()
	image=models.FileField()
	pub_on=models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug= slugify(self.title)
		super(BlogPost, self).save(*args,**kwargs)

class ContactDb(models.Model):
    subject=models.CharField(max_length=20,blank=True, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField(max_length=50)
    message=models.TextField()
    date_sent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.first_name} {self.last_name}, email: {self.email_address}"

class JoinDb(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField(max_length=50)
    affilate_uni=models.CharField(max_length=100)
    Date_of_Birth=models.DateTimeField()
    seg_id=models.PositiveIntegerField(blank=True, null=True, help_text="Renewers only !!")
    date_sent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.first_name} {self.last_name}, email: {self.email_address}"

