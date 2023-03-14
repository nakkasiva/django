from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=10)
    branch=models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.branch})"