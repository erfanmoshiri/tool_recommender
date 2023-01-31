from django.contrib.auth.models import User
from django.db.models import ForeignKey, CharField, CASCADE

from tools.models import BaseModel


class AuthCode(BaseModel):
    code = CharField(max_length=4)

    user = ForeignKey(
        User,
        related_name='codes',
        on_delete=CASCADE
    )
