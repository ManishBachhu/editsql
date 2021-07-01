from django.db import models

# Create your models here.
class EditSQL(models.Model):
    input_text = models.CharField(max_length=100)