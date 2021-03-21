from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group

class SoporteApitTest(TestCase):

    @classmethod
    def setUpClass(self):
        super(SoporteApitTest, self).setUpClass()
        self.user = User.objects.create(username='test')
        self.user.set_password('123')
        self.user.save()

    def test_listado_ticket(self):

        # Usuario sin loguearse
        response = self.client.get(reverse('list_tickets'))
        self.assertEqual(response.status_code, 403)

        # Usuario logueado pero sin permisos
        login = self.client.login(
            username='test', password='123')
        self.assertTrue(login)
        response = self.client.get(reverse('list_tickets'))
        self.assertEqual(response.status_code, 403)

        # Usuario logueado con persmisos
        with patch('apps.soporte.permissions.TicketsPermission.has_permission') as permission:
            permission.return_value = True
            response = self.client.get(reverse('list_tickets'))
            self.assertEqual(response.status_code, 200)