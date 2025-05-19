from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField()
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()
    plate = models.CharField(max_length=7, blank=True, null=True)
    value = models.FloatField()
   

    def __str__(self):
        return self.model
