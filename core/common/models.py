from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    created_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    updated_by = models.IntegerField(null=True)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.IntegerField(null=True)
    is_active = models.IntegerField(default=1, null=True)
    
    class Meta:
        abstract = True