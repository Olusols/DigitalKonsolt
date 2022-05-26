from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog_author_image = models.ImageField(upload_to='blog')
    description = models.TextField()
    post = RichTextField()
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    hitcount = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hitcount_generic_relation')
    
    tags = models.CharField(max_length=200)
    
    
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    
    date_added = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True, help_text='This is optional')
    
    
    comment_author_image = models.ImageField(
        upload_to='comment', null=True, blank=True, help_text='Colects the author image if any')
    
    
    # Colects the author website link if any
    author_website_url = models.URLField(
        null=True, blank=True, help_text='Collects the author website link if any')
    
    
    
    
