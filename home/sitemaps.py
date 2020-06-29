from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from .models import Service

class ServiceSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Service.objects.all()








