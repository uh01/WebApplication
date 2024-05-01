from django.db import models
from brands.models import BrandsModel
from django.contrib.auth.models import User

class CarsModel(models.Model):
    carName = models.CharField(max_length=255)
    carPrice = models.DecimalField(max_digits=10, decimal_places=0)
    carQuantity = models.PositiveIntegerField()
    carDescription = models.TextField()
    brands = models.ForeignKey(BrandsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/media/uploads/', blank = True, null = True)

    def __str__(self):
        return self.carName
    
class Comment(models.Model):
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
