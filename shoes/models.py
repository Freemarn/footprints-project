from django.db import models
from footUsers.models import FootUser
from django.utils.text import slugify 

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
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Shoe")
        verbose_name_plural = ("Shoes")

    def __str__(self):
        return f'{self.name} (brand-{self.brand})'


class SavedShoes(models.Model):
    shoes = models.ManyToManyField(Shoes)
    user = models.ForeignKey(FootUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'user({self.user})'
