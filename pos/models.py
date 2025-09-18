from django.db import models

class Category(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
