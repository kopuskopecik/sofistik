from django.shortcuts import render, get_object_or_404

from .models import (Setting, Service, Contact, About, Mission, 
Partner, Feature, Testimonial, CompanyType, Reference, Member)
# Create your views here.
def home(request):
    setting  = Setting.objects.first()
    services = Service.objects.filter(service_or_not=True)
    solutions = Service.objects.filter(service_or_not=False)
    contact = Contact.objects.first()
    about = About.objects.first()
    missions = Mission.objects.all()
    partners = Partner.objects.all()
    company_types = CompanyType.objects.all()
    references = Reference.objects.all()
    

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
    service = get_object_or_404(Service, slug = slug)
    services = Service.objects.filter(service_or_not=True)
    solutions = Service.objects.filter(service_or_not=False)
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