from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import LogForm
from .models import Category


class TestCategoriesViews(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        self.category = Category(name="test-name", slug="test-name")
        self.category.save()

    def test_render_category_detail_page_with_log_form(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'category_detail', args=['test-name']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test-name", response.content)
        self.assertIsInstance(
            response.context['log_form'], LogForm)
