from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

# Create your models here.

FONTS = (

	("icofont-computer", "bilgisayar"),
	("icofont-chart-bar-graph", "grafik"),
	("icofont-image", "resim"),
	("icofont-settings", "ayar"),
	("icofont-earth", "dünya"),
	("icofont-tasks-alt", "alt görev"),
    ("icofont-award", "ödül"),
    ("icofont-clock-time", "saat"),
    ("icofont-document-folder", "dosya"),
    ("icofont-simple-smile", "gülücük"),
    ("ri-brush-4-line", "mission"),
    ("ri-movie-2-line", "film şeridi"),
    ("ri-calendar-check-line", "takvim"),


)

class Setting(models.Model):
    title = models.CharField("title", max_length=50)
    icon = models.ImageField("İcon", upload_to='setting/')
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    image = models.ImageField("Ana sayfadaki büyük resim", upload_to='setting/')
    youtube_url = models.URLField("anasayfadaki URL adresi")
    header = models.CharField("ana sayfadaki resim üstündeki başlık", max_length=150, blank=True)
    content = models.CharField("ana sayfadaki resim üsütündeki içerik", max_length=150, blank=True)
    get_startted = models.CharField("Nabvardaki get_started", default = "Get Started", max_length=50)
    about = RichTextField()
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    skype_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    copyright_name = models.CharField(max_length=50, default="Sofistech")
    adresse = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField("hakkımızda başlığı", max_length=150)
    sub_content = models.CharField("hakkımızda alt metin", max_length=250)
    content = RichTextField("içerik")
    about_image = models.ImageField("Hakkımızda kısmında çıkacak olan resim")
    about_youtube_url = models.URLField("Hakkımızda ile ilgili olan youtube URL'i ")

    def __str__(self):
        return self.title

class AboutLogo(models.Model):
    title = models.CharField("açıklama", max_length=50)
    font = models.CharField(max_length=50, choices=FONTS)
    about = models.ForeignKey("About", on_delete =models.CASCADE)
    number = models.IntegerField(default = 0)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField("Vizyon başlığı", max_length=30)
    content = models.CharField("içerik", max_length=150)
    about_image = models.ImageField("resim")
    

    def __str__(self):
        return self.title


class Partner(models.Model):
    title = models.CharField("İş ortağının adı:", max_length=50, unique=True)
    content = RichTextField("Ortak hakkında bilgi")
    image = models.ImageField()
    slug = models.SlugField(editable = False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Partner, self).save(*args, **kwargs)


class Service(models.Model):
    title = models.CharField("Hizmetin adı:", max_length=50, unique=True)
    font = models.CharField(max_length=50, choices=FONTS)
    content = RichTextField("Servis hakkında bilgi")
    image = models.ImageField()
    slug = models.SlugField(editable = False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)


class Solution(models.Model):
    title = models.CharField("Çözüm adı:", max_length=50, unique=True)
    font = models.CharField(max_length=50, choices=FONTS)
    content = RichTextField("Çözüm hakkında bilgi")
    image = models.ImageField()
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Solution, self).save(*args, **kwargs)


class Reference(models.Model):
    title = models.CharField("Referansın adı:", max_length=50, unique=True)
    content = RichTextField("Referans hakkında bilgi")
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        super(Reference, self).save(*args, **kwargs)




class Member(models.Model):
    name = models.CharField("isim", max_length=50)
    email = models.EmailField()
    number = models.CharField("Telefon Numarası", max_length=30)

    def __str__(self):
        return self.name

class Contact(models.Model):
    member = models.ManyToManyField('Member')
    addresse = models.CharField("adres", max_length=150)


