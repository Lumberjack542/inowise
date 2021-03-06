from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ticket(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    completed = models.BooleanField(default=False)
    frozen = models.BooleanField(default=False)
    unresolved = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'