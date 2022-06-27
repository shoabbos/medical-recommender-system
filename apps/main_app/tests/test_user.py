from django.test import TestCase
from django.contrib.auth.models import User

from ..models import rate_review


class UserTestCase(TestCase):
    def setUp(self):
    	User.objects.create_user("testingUser", "test@mail.ru", "passweord232Sfwew2")

    def test_user_saved_correctly(self):
        """Test user"""
        user = User.objects.get(username="testingUser")
        self.assertEqual(user.username, 'testingUser')
