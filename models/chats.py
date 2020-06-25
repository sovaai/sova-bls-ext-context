from tortoise.models import Model
from tortoise import fields
from uuid import uuid4


class Chat(Model):
    """

    """
    id = fields.IntField(pk=True)
    cuid = fields.UUIDField(default=uuid4, unique=True)
    context = fields.JSONField(default={})
    inf = fields.ForeignKeyField('models.Infs')
    technical_context = fields.JSONField(default={})

    @property
    def cuid_str(self):
        return f"{self.cuid}"