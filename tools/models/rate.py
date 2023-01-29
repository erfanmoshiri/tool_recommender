from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField, IntegerField, ForeignKey, CASCADE

from tools.models import BaseModel


class Rate(BaseModel):
    rate = IntegerField()

    user = ForeignKey(
        User,
        related_name='rates',
        on_delete=CASCADE
    )
    tool = ForeignKey(
        'tools.Tool',
        related_name='rates',
        on_delete=CASCADE
    )
