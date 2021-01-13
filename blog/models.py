from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


from ckeditor.fields import RichTextField



class Category(models.Model):
    title = models.CharField("başlık", max_length=100, unique=True)
    slug = models.SlugField(editable = False)
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse('blog:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        

class Tag(models.Model):
    title = models.CharField("başlık", max_length=50, unique = True)
    slug = models.SlugField(editable = False)

    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagler'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('blog:tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)                   



class Blog(models.Model):
    category = models.ForeignKey("Category", on_delete =models.CASCADE)
    user = models.ForeignKey(User, on_delete =models.CASCADE) 
    title = models.CharField("başlık", max_length=150, unique = True)
    slug = models.SlugField(editable = False)
    sub_content = models.CharField("Giriş metni", max_length=150)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    image = models.ImageField("Resim", upload_to='setting/')
    content = RichTextField("Uzun içerik")
    blogs = models.ManyToManyField("self", blank = True)
    tags = models.ManyToManyField("Tag", blank = True)
    publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
    updating_date = models.DateTimeField(verbose_name="güncellenme_tarihi", auto_now = True)
    active = models.BooleanField("Sitede gözükmesi için tıklayınız", default = False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
 
    

