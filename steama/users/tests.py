from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='admin',
            email='admin@admin.by',
            password='testpass123'
        )
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@admin.by')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_user(
            username='superadmin',
            email='superadmin@superadmin.by',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@superadmin.by')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)