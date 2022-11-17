from django.db import models
from django.utils.translation import gettext_lazy as _


class IsActiveFlagChoices(models.IntegerChoices):
    """
    All choices for `is_active` field of SoftDeleteModel.
    """
    ACTIVE = 1, _('Active')
    DELETED = 0, _('Deleted')