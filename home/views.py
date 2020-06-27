from django.shortcuts import render

from .models import Setting, Service, Solution, Contact, About, Mission, Partner, Feature
# Create your views here.
def home(request):
    setting  = Setting.objects.first()
    services = Service.objects.all()
    solutions = Solution.objects.all()
    contact = Contact.objects.first()
    about = About.objects.first()
    missions = Mission.objects.all()
    partners = Partner.objects.all()
    

    context = {
        'setting': setting,
        'services': services,
        'solutions': solutions,
        'contact': contact,
        'about': about,
        'missions': missions,
        'partners': partners,
		
	}
    if setting.features:
        features = Feature.objects.all()
        context["features"] = features
    return render(request, 'index.html', context)