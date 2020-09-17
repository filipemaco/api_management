from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class IncomeStatement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    profit = models.FloatField(null=True, blank=True)
    loss = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
