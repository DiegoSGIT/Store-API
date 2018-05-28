import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


def minutesToExpire():
    return timezone.now() + timezone.timedelta(minutes=10)


class TokenActivate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(null=False, unique=True, max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField(default=minutesToExpire)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)