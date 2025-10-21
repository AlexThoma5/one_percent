from django.test import TestCase
from .forms import LogForm


class TestLogForm(TestCase):

    def test_form_is_valid_with_only_title(self):
        """Test for the required 'title' field"""
        log_form = LogForm({'title': 'Went for a run'})
        self.assertTrue(
            log_form.is_valid(), msg='Form is not valid with title')

    def test_form_is_valid_with_title_and_content(self):
        """Test all fields"""
        log_form = LogForm({'title': 'Went for a run',
                            'content': 'run lasted 30 mins total'})
        self.assertTrue(log_form.is_valid(),
                        msg='Form is not valid with title and content')

    def test_form_is_invalid_without_title(self):
        """Negative test for the 'title' field"""
        log_form = LogForm({'title': '',
                            'content': 'run lasted 30 mins total'})
        self.assertFalse(log_form.is_valid(),
                         msg='Form is valid without title')
