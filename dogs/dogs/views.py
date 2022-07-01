from django.http import JsonResponse
from .models import Dog
from .serializers import DogSerializer, DogImageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random

@api_view(['GET', 'POST'])
def dog_list(request, format = None):

    #get all the dogs
    #serialize them
    #return json

    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def dog_detail(request, id, format = None):

    try:
        dog = Dog.objects.get(pk = id)

    except Dog.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DogSerializer(dog, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def dog_random(request, format = None):
    
    allDogs = Dog.objects.count()

    try:
        dog = Dog.objects.get(pk = random.randint(1, allDogs))

    except Dog.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DogImageSerializer(dog)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DogImageSerializer(dog, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)