from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="First meal")
        DishType.objects.create(name="Side dishes")

        response = self.client.get(DISH_TYPE_URL)
        dishes_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dishes_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")
