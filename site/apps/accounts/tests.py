from django.test import TestCase

from .models import User


strings = list('abc')


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username=strings[0],
        )

    def test_fields_exist(self):
        self.assertIsNotNone(self.user.password)
        self.assertIsNotNone(self.user.email)
        self.assertIsNotNone(self.user.first_name)
        self.assertIsNotNone(self.user.last_name)
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_service)
        self.assertTrue(self.user.is_active)
        self.assertIsNotNone(self.user.date_joined)
        self.assertIsNone(self.user.last_login)
        self.assertIsNotNone(self.user.user_permissions)
