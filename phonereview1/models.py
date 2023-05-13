from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    manufacturing_date = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PhoneModel(models.Model):
    name = models.CharField(max_length=50)
    launch_date = models.DateField()
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name


class Review(models.Model):
    phone_name = models.ForeignKey(
        PhoneModel, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.review)[:150]
        super().save(*args, **kwargs)
