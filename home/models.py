from django.db import models
from django.utils.text import slugify
from django.urls import reverse

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
    get_startted = models.CharField("Navbardaki get_started", default = "Get Started", max_length=50)
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
    features = models.BooleanField("Özellikler kısmının gözükmesini istiyorsanız tıklayınız:", default=False)
    testimonials = models.BooleanField("Müşteri yorumlarının sergilenmesi için tıklayınız.", default=False)
    teams = models.BooleanField("Sofistech ekibinin segilenmesi için tıklayınız.", default=False)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField("hakkımızda başlığı", max_length=150)
    sub_content = models.CharField("hakkımızda alt metin", max_length=250)
    content = RichTextField("içerik")
    about_image = models.ImageField("Hakkımızda kısmında çıkacak olan resim")
    about_youtube_url = models.URLField("Hakkımızda ile ilgili olan youtube URL'i ")

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızdakiler'

    def __str__(self):
        return self.title

class AboutLogo(models.Model):
    title = models.CharField("açıklama", max_length=50)
    font = models.CharField(max_length=50, choices=FONTS)
    about = models.ForeignKey("About", on_delete =models.CASCADE)
    number = models.IntegerField(default = 0)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Hakkımızdada Bulunan Font'
        verbose_name_plural = 'Hakkımızdada Bulunan Fontlar'

    def __str__(self):
        return self.title


class Mission(models.Model):
    MISSION_FONTS = (
        ("ri-brush-4-line", "mission"),
        ("ri-movie-2-line", "film şeridi"),
        ("ri-calendar-check-line", "takvim"),
    )
    title = models.CharField("Vizyon başlığı", max_length=30)
    content = models.CharField("içerik", max_length=150)
    font = models.CharField(max_length=50, choices=MISSION_FONTS)
    image = models.ImageField("resim")

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Vizyon'
        verbose_name_plural = 'Vizyonlar'

    

    def __str__(self):
        return self.title


class Partner(models.Model):
    title = models.CharField("İş ortağının adı:", max_length=50)
    image = models.ImageField()

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'İş Ortağı'
        verbose_name_plural = 'İş Ortakları'


    def __str__(self):
        return self.title

class Feature(models.Model):

    FEATURE_FONTS = (
        ("ri-gps-line", "gps"),
        ("ri-body-scan-line", "body"),
        ("ri-sun-line", "güneş"),
        ("ri-store-line", "dükkan"),
    )

    font_title = models.CharField("Font Başlık", max_length=50)
    font = models.CharField(max_length=50, choices=FEATURE_FONTS)
    title = models.CharField("Başlık:", max_length=50)
    sub_content = models.CharField("üst içerik", max_length=150)
    content = RichTextField("İçerik")
    image = models.ImageField()
    ranking = models.SmallIntegerField("sıralama", unique=True)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Ekstra Özellikler'
        verbose_name_plural = 'Özellikler'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField("Hizmetin adı:", max_length=50, unique=True)
    font = models.CharField(max_length=50, choices=FONTS)
    home_content = models.CharField(max_length=250, default = "Kısa Açıklama")
    content = RichTextField("Servis hakkında bilgi")
    image = models.ImageField()
    slug = models.SlugField(editable = False)
    service_or_not = models.BooleanField("Hizmet ise tıklanacak değilse Tıklanmayacak", default = False)
    software = models.BooleanField("Yazılım Hizmetleri için tıklanacak", default = False)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)    
    active = models.BooleanField("Sitede gösterilsin mi", default = False)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Hizmet ve Çözüm'
        verbose_name_plural = 'Hizmet ve Çözümlerimiz'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'slug':self.slug})



class Testimonial(models.Model):
    image = models.ImageField("Müşteri resmi")
    title = models.CharField("Müşteri adı", max_length=50)
    sub_title = models.CharField("Müşteri Ünvanı", max_length=50)
    content = models.CharField("Müşteri Yorumu", max_length=150)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Müşteri Görüşü'
        verbose_name_plural = 'Müşteri Görüşleri'

    def __str__(self):
        return self.title



class CompanyType(models.Model):
    title = models.CharField("Şirket tipi", max_length=10)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Şirket Tipi'
        verbose_name_plural = 'Şirket Tipleri'
    
    def __str__(self):
        return self.title

class Reference(models.Model):
    title = models.CharField("Referansın adı:", max_length=50)
    content = models.CharField("Referansın kısa açıklaması:", max_length=75)
    image = models.ImageField("Referans resmi")
    company_type = models.ForeignKey('CompanyType', on_delete=models.CASCADE)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Referans'
        verbose_name_plural = 'Referanslar'

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField("isim", max_length=50)
    job = models.CharField("ünvan", max_length=50)
    email = models.EmailField()
    number = models.CharField("Telefon Numarası", max_length=30)
    image = models.ImageField("Profil resmi", blank=True, null=True)
    twitter_url = models.URLField(blank = True)
    facebook_url = models.URLField(blank = True)
    instagram_url = models.URLField(blank = True)
    linkedin_url = models.URLField(blank = True)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Sofistech Üye'
        verbose_name_plural = 'Sofistech Üyeleri'

    def __str__(self):
        return self.name

class Contact(models.Model):
    member = models.ManyToManyField('Member')
    addresse = models.CharField("adres", max_length=150)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim Bilgileri'

    


class ContactInfo(models.Model):
    name = models.CharField("İsminiz:", max_length=40)
    email = models.EmailField("Email:")
    topic = models.CharField("Konu:", max_length = 150)
    content = models.TextField("Mesajınız:")

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Gelen Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'

    def __str__(self):
        return self.name


