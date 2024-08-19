from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# - Name
# - Description
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"


# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)

class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, 
        on_delete=models.CASCADE
    )  # Many-to-One relationship

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(
        max_length=10, 
        choices=CAR_TYPES, 
        default='SUV'
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.name} ({self.year})"
    