from django.shortcuts import render

from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from rest_framework import serializers, viewsets


# Define a serializer for the photo model.
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'image', 'created_at', 'updated_at')

# Define a viewset for the photo model.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

# Define a view function that accepts photos and saves them in the file system and also inserts it in the database.
@require_http_methods(['POST'])
def upload_photo(request):
    # Get the photo from the request.
    photo = request.FILES['photo']

    # Save the photo in the file system.
    with open('photos/' + photo.name, 'wb') as f:
        f.write(photo.read())

    # Insert the photo in the database.
    photo_model = Photo(title=photo.name, image=photo)
    photo_model.save()

    return HttpResponse('Photo uploaded successfully.')
