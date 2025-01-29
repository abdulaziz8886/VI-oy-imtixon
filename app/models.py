from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class bascet(models.Model):
    user = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='bascet/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    rang = models.CharField(max_length=50)
    razmer = models.CharField(max_length=5)
    narx = models.PositiveBigIntegerField()
    soni = models.PositiveIntegerField()
    jami = models.PositiveBigIntegerField(null=True, blank=True)



class like(models.Model):
    user = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='likes/')
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=255)
    narx = models.CharField(max_length=255)

class categorygander(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

class categorySale(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("category2", args=[self.slug])

class categoryProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("category3", args=[self.slug])

class categoryRazmer(models.Model):
    name = models.CharField(max_length=1)
    slug = models.SlugField(max_length=1, unique=True)
    def __str__(self):
        return self.name
    
class categoryRang(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    def __str__(self):
        return self.name

class products(models.Model):
    rasm = models.ImageField(upload_to='product', help_text='Hurmatli admin rasm jo\'natayotganingizda rasm 800x600 razmerida bo\'lsin')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(categorygander, on_delete=models.CASCADE)
    category1 = models.ForeignKey(categorySale, on_delete=models.CASCADE)
    category2 = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True, blank=True)  
    razmer = models.ManyToManyField(to=categoryRazmer)
    description = models.TextField()
    rang = models.ManyToManyField(to=categoryRang)
    narx = models.PositiveBigIntegerField()

    


    def __str__(self):
        return self.title

class comentuser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    izoh = models.TextField()


    def __str__(self):
        return self.name