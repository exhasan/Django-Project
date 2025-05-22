from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    # Add more fields as needed

    def __str__(self):
        return self.title