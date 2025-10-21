from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase


class TestHomeView(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

    def test_redirects_authenticated_user_to_dashboard(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_redirects_anon_user_to_landing(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('landing'))


class TestDashboardView(TestCase):

    def setUp(self):
        """ Creates user instance for tests"""
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

    def test_render_dashboard_page_with_categories(self):
        """ Test for dashboard page rendering with correct context
        and template """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

        # checks for content and context
        self.assertIn(b"myUsername", response.content)
        self.assertIn("categories", response.context)
        self.assertIn("log_count", response.context)
        self.assertIn("labels", response.context)
        self.assertIn("data", response.context)


class TestLandingView(TestCase):
    """ Test for landing page rendering with correct template """
    def test_renders_landing_template(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/landing.html")
