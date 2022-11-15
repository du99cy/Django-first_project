from django.db import models

from common.models import TimeStampedModel


# Create your models here.
class ContainerType(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    tenant_id = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'container_type'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'tenant_id', 'is_active'),
                name='name__tenant_id__uq'
            )
        ]