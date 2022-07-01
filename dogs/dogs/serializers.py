from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'dog_name', 'dog_image']


class DogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'dog_image']

