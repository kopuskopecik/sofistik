"""sofistik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from home.sitemaps import ServiceSitemap


sitemaps = {
	'services' : ServiceSitemap,

}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type ="text/plain")),
    path('googleb2c85495126fb742.html', TemplateView.as_view(template_name="googleb2c85495126fb742.html")),
    path('samz0cq0ohwg3s88qsh5nv4fc1ysvd.html', TemplateView.as_view(template_name="samz0cq0ohwg3s88qsh5nv4fc1ysvd.html")),
    path('blog/', include('blog.urls')),

    path('', include('home.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
