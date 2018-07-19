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


#
# if using token-based authentication with the REST framework, uncomment the following section
#

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
