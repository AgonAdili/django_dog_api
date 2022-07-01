from django.db import models

class Dog(models.Model):
    dog_name = models.CharField(max_length = 50)
    dog_image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.dog_name