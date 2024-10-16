from django.db import models
from django.conf import settings


class Lake(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Rock(models.Model):
    # lake = models.ForeignKey(Lake, on_delete=models.CASCADE, related_name='rocks', null=True, blank=True, default=1)    
    lake = models.ForeignKey(Lake, on_delete=models.CASCADE, related_name='rocks')
    name = models.CharField(max_length=50, blank=True)
    marker_id = models.CharField(max_length=10, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True)
    depth = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    size = models.PositiveIntegerField(blank=True)
    
    STATUS_CHOICES = [
        ('marked', 'Marked'),
        ('missing', 'Missing'),
        ('candidate', 'Candidate'),
        ('other', 'Other'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    more_info = models.TextField(blank=True)
    
    def __str__(self):
        return self.name