from django.contrib.auth.models import User
from django.db.models import ForeignKey, BooleanField, DateTimeField, CASCADE

from tools.models import BaseModel


class Recommend(BaseModel):
    user = ForeignKey(
        User,
        related_name='recommends',
        on_delete=CASCADE
    )

    tool = ForeignKey(
        'tools.Tool',
        related_name='recommends',
        on_delete=CASCADE
    )

    feature = ForeignKey(
        'tools.Feature',
        related_name='recommends',
        on_delete=CASCADE
    )

    liked = BooleanField(
        null=True
    )

    created = DateTimeField(auto_now_add=True)
