from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"


