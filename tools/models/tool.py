from django.db import models

from tools.models import BaseModel


class Tool(BaseModel):
    Title = models.CharField(
        max_length=128,
    )
