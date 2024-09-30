from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Car(models.Model):

    class CarType(models.TextChoices):
        HATCH = "hatch", "Hatch"
        SEDAN = "sedan", "Sedan"
        SUV = "suv", "SUV"
        PICKUP = "pickup", "Pickup"

    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand", default="")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    car_type = models.CharField(blank=True, null=True, max_length=50, choices=CarType.choices)
    plate = models.CharField(blank=True, null=True, max_length=10)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    foto = models.ImageField(upload_to='cars/', blank=True, null=True)
    picture = models.ImageField(upload_to='cars/', blank=True, null=True)
    observations = models.CharField(blank=True, null=True, max_length=250)
    active = models.BooleanField(default=False)

def __str__(self):
    return self.model
    