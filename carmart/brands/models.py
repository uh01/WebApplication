from django.db import models

class BrandsModel(models.Model):
    brandName = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.brandName
