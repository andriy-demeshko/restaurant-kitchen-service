from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import Cook

COOK_URL = reverse("kitchen:cook-list")


class PublicCookTests(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_cook(self):
        get_user_model().objects.create_user(
            username="master_chiff",
            password="password123",
            first_name="Dick",
            last_name="Wild",
            years_of_experience=35
        )

        response = self.client.get(COOK_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
