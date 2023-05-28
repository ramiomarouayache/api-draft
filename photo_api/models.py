from django.db import models

# Define a photo model.
class Photo(models.Model):
    title = models.CharField(max_length=255)
    refrence = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by =

    class Meta:
        db_table = 'photo'