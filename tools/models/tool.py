from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField, ManyToManyField

from tools.models import BaseModel


class Tool(BaseModel):
    Title = models.CharField(
        max_length=128,
    )
    Company = models.CharField(
        max_length=128,
        null=True
    )
    Description = TextField(null=True)
