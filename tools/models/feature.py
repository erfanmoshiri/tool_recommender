from django.db.models import CharField

from tools.models import BaseModel


class Feature(BaseModel):
    name = CharField(
        max_length=64
    )
    