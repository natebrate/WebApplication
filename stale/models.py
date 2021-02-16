from django.db import models


# Create your models here

class Staff(models.Model):
    ROLE = (
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
    )
    id = models.AutoField(null=False, primary_key=True)
    user = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True, choices=ROLE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    FEEDING = (
        ('Herbivores', 'Herbivores'),
        ('Omnivores', 'Omnivores'),
        ('Carnivores', 'Carnivores'),
    )
    name = models.CharField(max_length=200, null=True)
    feedingType = models.CharField(max_length=200, null=True, choices=FEEDING)
    quantity = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    SEX = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    name = models.CharField(max_length=200, null=True)
    trainerID = models.IntegerField(null=True)
    species = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=200, null=True, choices=SEX)
    weight = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
