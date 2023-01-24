from django.db.models import Model, BooleanField


class BaseModel(Model):
    is_deleted = BooleanField(
        default=False,
        null=False,
    )

    class Meta:
        abstract = True
