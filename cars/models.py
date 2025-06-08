from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=7, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits='10', decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):                                    
        return f'{self.cars_count}  -   {self.cars_values}'
    