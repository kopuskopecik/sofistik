from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import (Setting, Service, Contact, About, Mission, 
Partner, Feature, Testimonial, CompanyType, Reference, Member)
from .forms import ContactForm


# Create your views here.
def home(request):
    setting  = Setting.objects.first()
    services = Service.objects.filter(service_or_not=True, active = True)
    solutions = Service.objects.filter(service_or_not=False, active = True)
    contact = Contact.objects.first()
    about = About.objects.first()
    missions = Mission.objects.all()
    partners = Partner.objects.all()
    company_types = CompanyType.objects.all()
    references = Reference.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarı bir şekilde mesajınız tarafımıza iletilmiştir. En kısa sürede sizinle iletişime geçilecektir.')
            return redirect("/")
    else:
        form = ContactForm()
    

    context = {
        'setting': setting,
        'services': services,
        'solutions': solutions,
        'contact': contact,
        'about': about,
        'missions': missions,
        'partners': partners,
        'company_types': company_types,
        'references': references,
        'form': form, 
		
	}
    if setting.features:
        features = Feature.objects.all()
        context["features"] = features
    if setting.testimonials:
        testimonials = Testimonial.objects.all()
        context["testimonials"] = testimonials
    if setting.teams:
        members = Member.objects.all()
        context["members"] = members

    return render(request, 'index.html', context)


def detail(request, slug):
    setting  = Setting.objects.first()
    service = get_object_or_404(Service, slug = slug, active = True)
    services = Service.objects.filter(service_or_not=True, active = True)
    solutions = Service.objects.filter(service_or_not=False, active = True)
    #contact = Contact.objects.first()
    #about = About.objects.first()
    #missions = Mission.objects.all()
    partners = Partner.objects.all()
    

    context = {
        'setting': setting,
        'services': services,
        'solutions': solutions,
        #'contact': contact,
        #'about': about,
        #'missions': missions,
        'partners': partners,
        'service': service,
		
	}

    return render(request, 'detail.html', context)