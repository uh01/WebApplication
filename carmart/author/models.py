from django.db import models
from cars.models import CarsModel
from django.contrib.auth.models import User

class BoughtCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} bought {self.car.carName}"