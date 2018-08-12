import logging

from django.contrib.auth.models import AbstractUser
from django.db import models


log = logging.getLogger(__name__)


class User(AbstractUser):

    is_service = models.BooleanField(
        default=False,
        verbose_name='Service status',
        help_text='Designates whether this user can execute automated administrative tasks.',
    )

    class Meta:
        ordering = ('username',)
