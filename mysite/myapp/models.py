from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Blog(models.Model):
    title = models.CharField(max_length=255)
    media_file = models.FileField(upload_to='media/', default='default_value.mp4')
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PartyService(models.Model):
    title_p = models.CharField(max_length=255, blank=True, null=True)
    media_file_p = models.FileField(upload_to='media/', default='default_value.mp4')
    text_p = models.TextField()

    def __str__(self):
        return self.title_p


class Section(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    custom_index = models.CharField(max_length=30, blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    custom_index = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DishGallery(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/', default='default_image.jpg')

    def __str__(self):
        return self.name


class Impressum(models.Model):
    responsible = models.TextField()
    contact_us = models.TextField()
    internet = models.TextField()
    telephone = models.TextField()

    def __str__(self):
        return self.responsible


@receiver(pre_save, sender=Impressum)
def limit_impressum_objects(sender, instance, **kwargs):
    existing_objects = Impressum.objects.exclude(id=instance.id)
    if existing_objects.exists():
        raise ValidationError('Может быть создан только один объект Impressum.')
