from django.shortcuts import render, redirect
from .models import Service, Project, Testimonial, Team
from django.views import generic

SOME_INFO  = {
    'phone_number': '2349064882793',
    'address': 'Ibadan, Nigeria',
    'contact_info' : 'digitalkonsolt@gmail.com',
    
    'satisfied_client': 20,
    'project_completed': 35,
    'countries': 2,
}
def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    
    testimonial = Testimonial.objects.all()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonial': testimonial,
        'info': SOME_INFO,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'konsolt/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('msg_subject')
        message = request.POST.get('message')
        
        from Konsolt.models import Contact
        
        contact = Contact(name=name, email=email, phone =phone_number, subject=subject, message=message)
        contact.save()
        
        return redirect('success')
        
       
    
        
    return render(request, 'konsolt/contact.html')

def success(request):
    return render(request, 'konsolt/success.html')

def privacyPolicy(request):
    return render(request, 'konsolt/privacy-policy.html')


def termsCondition(request):
    return render(request, 'konsolt/terms-condition.html')




def service(request):
    services = Service.objects.all()
    
    context = {
        'services': services
    }
    return render(request, 'konsolt/service.html', context)

class ServiceDetail(generic.DetailView):
    model = Service
    template_name = 'service-detail.html'
    context_object_name = 'service'
    


def works(request):
    works = Project.objects.all()
    
    context = {
        'works': works,
    }
    return render(request, 'konsolt/work.html', context)


class WorkDetail(generic.DetailView):
    model = Project
    template_name = 'work-detail.html'
    context_object_name = 'project'
    
    
    
def faq(request):
    return render(request, 'konsolt/faq.html')

def testimonial(request):
    team = Team.objects.all()
    
    context = {
        'team': team,
    }
    return render(request, 'konsolt/testimonials.html', context)

