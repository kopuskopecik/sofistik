from django.shortcuts import render

from .models import Setting, Service, Solution, Contact, About
# Create your views here.
def home(request):
    setting  = Setting.objects.first()
    services = Service.objects.all()
    solutions = Solution.objects.all()
    contact = Contact.objects.first()
    about = About.objects.first()

    context = {
        'setting': setting,
        'services': services,
        'solutions': solutions,
        'contact': contact,
        'about': about,
		
	}
    return render(request, 'index.html', context)