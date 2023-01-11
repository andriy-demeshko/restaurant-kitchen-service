from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook123",
            years_of_experience="10"
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_create_additional_info_listed(self):
        url = reverse("admin:kitchen_cook_add")
        res = self.client.get(url)

        self.assertContains(res, "first_name")
        self.assertContains(res, "last_name")
        self.assertContains(res, "years_of_experience")
