from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from categories.models import Category


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
