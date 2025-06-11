from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value_car=Sum('value')
    )['total_value_car']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.bio = ai_bio
        print('1')
@receiver(post_save, sender=Car)
def post_save_car(sender, instance,**kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def post_delete_car(sender, instance, **kwargs):
    car_inventory_update()