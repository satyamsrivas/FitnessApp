from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    class ObjectStatusTypeChoices(models.IntegerChoices):
        ACTIVE = 1, "Active"
        DELETED = 2, "Deleted"
        
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    object_status = models.PositiveIntegerField(choices=ObjectStatusTypeChoices.choices,default=ObjectStatusTypeChoices.ACTIVE)

    class Meta:
        abstract = True
