from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    source_website = models.CharField(max_length=200)  
    source_url = models.URLField(unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']

