from time import strftime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.user.username


class Dweet(models.Model):
    user = models.ForeignKey(User, related_name='dweets', on_delete=models.DO_NOTHING)
    text = models.CharField(verbose_name='Dweet text', max_length=140)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.created_at.strftime('%Y-%b-%d, %H:%M')} {self.text}"
