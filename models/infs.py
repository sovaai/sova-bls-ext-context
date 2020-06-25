from tortoise.models import Model
from tortoise import fields
from uuid import uuid4


class Infs(Model):
    """
        Таблица инфов.
    """
    id = fields.IntField(pk=True)
    uuid = fields.UUIDField(default=uuid4, unique=True, null=False)
    inf_profile = fields.CharField(null=False, max_length=254)

    @property
    def uuid_str(self):
        return f"{self.uuid}"
