from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_add_fields_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test name",
            "last_name": "Test last",
            "years_of_experience": 49
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
