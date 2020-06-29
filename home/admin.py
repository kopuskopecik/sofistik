from django.contrib import admin

from .models import (Setting, Partner, Service, Reference, Member, Contact, About, 
AboutLogo, Mission, Feature, Testimonial, Reference, CompanyType, ContactInfo) 

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'icon', 'youtube_url','header', 'content', 'description']


class ServiceAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'font','image', 'home_content', 'active']
	list_editable = ['font', 'image','home_content', 'active']


class ContactAdmin(admin.ModelAdmin):
		
	list_display = ["addresse"]




admin.site.register(Setting, SettingAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Member)
admin.site.register(About)
admin.site.register(AboutLogo)
admin.site.register(Mission)
admin.site.register(Partner)
admin.site.register(Feature)
admin.site.register(Testimonial)
admin.site.register(Reference)
admin.site.register(CompanyType)
admin.site.register(ContactInfo)



	