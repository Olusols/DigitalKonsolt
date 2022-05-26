from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('privacy-policy/', views.privacyPolicy, name='privacy-policy'),
    path('terms-condition', views.termsCondition, name='terms'),
    
    
    path('service/',views.service, name='service' ),
    path('service/<int:pk>/<slug:slug>/', views.ServiceDetail.as_view(), name='service-detail'),
    
    path('work', views.works, name='work'),
    path('work/<int:pk>/<slug:slug>/', views.WorkDetail.as_view(), name='work-detail'),
    
    
    path('success', views.success, name='success'),
    
    path('faq/', views.faq, name='faq'),
    path('testimonial/', views.testimonial, name='testimonial')
]


