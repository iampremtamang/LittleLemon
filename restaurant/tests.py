from django.test import TestCase

from .models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self) -> None:
        item = Menu.objects.create(title='Icecream', price=80, inventory=100)
        self.assertEqual(item.__str__(), "Icecream : 80")
