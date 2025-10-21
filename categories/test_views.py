from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import LogForm
from .models import Category


class TestCategoriesViews(TestCase):

    def setUp(self):
        """ Creates user and test category """
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        self.category = Category(name="test-name", slug="test-name")
        self.category.save()

    def test_render_category_detail_page_with_log_form(self):
        """ Verifies get request for category_detail page
        containing the log_form """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'category_detail', args=['test-name']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test-name", response.content)
        self.assertIsInstance(
            response.context['log_form'], LogForm)

    def test_successful_log_submission(self):
        """ Test for posting a log on a category """
        self.client.login(username="myUsername", password="myPassword")
        log_data = {
            'title': 'This is a test log.'
        }
        response = self.client.post(reverse(
            'category_detail', args=['test-name']), log_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Great job! Your new log has been added.',
            response.content
        )
