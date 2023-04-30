from django.db import models
from footUsers.models import FootUser
from django.utils.html import mark_safe

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField( upload_to='images/logo')

    class Meta:
            verbose_name = ("Brand")
            verbose_name_plural = ("Brands")

    def __str__(self):
        return self.name


class Shoes(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='images/shoe')
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Categories)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)

    def img_preview(self): 
        print(self.image.url)
        return mark_safe(f'<a href="{self.image.url}"><img src = "{self.image.url}" width = "250"/> Click To Preview</a>')


    class Meta:
        verbose_name = ("Shoe")
        verbose_name_plural = ("Shoes")

    def __str__(self):
        return f'{self.name} (brand-{self.brand})'


class SavedShoes(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    user = models.ForeignKey(FootUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'shoe(shoes) saved by {self.user}'
