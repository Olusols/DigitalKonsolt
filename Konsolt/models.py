from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

SERVICES = [
    
]



class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    service = models.ManyToManyField('Service')
    
    details = RichTextField()
    
    picture = models.ImageField(upload_to='project')
    
    @property
    def get_absolute_url(self):
        slug = slugify(self.name)
        return reverse('work-detail', args=[self.pk, slug])

    
    
class Service(models.Model):
    CATEGORY = [
        ('',''),
    ]
    service = models.CharField(max_length=40, choices=SERVICES)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY)
    picture = models.ImageField(upload_to='service')
    icon = models.TextField()
    description = models.TextField()
    details = RichTextField()
    
    @property
    def get_absolute_url(self):
        slug = slugify(self.service)
        return reverse('service-detail', args=[self.pk, slug])
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    rate = models.IntegerField()
    picture = models.ImageField(upload_to='testimonial')
    feedback = models.TextField()
    


class Team(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='team')
    role = models.CharField(max_length=30)
    
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
