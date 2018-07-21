import logging

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from django.db import models


log = logging.getLogger(__name__)


class User(GaeAbstractDatastoreUser):

    is_service = models.BooleanField(
        default=False,
        verbose_name='Service status',
        help_text='Designates whether this user can execute automated administrative tasks.',
    )

    class Meta:
        ordering = ('username',)
