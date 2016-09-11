from django.test import TestCase

from .models import User
from .templatetags.users_tags import eligible, bizzfuzz

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="max@masters.com", birthday="1990-06-22")
        User.objects.create(email="kid@masters.com", birthday="2011-06-04")

    def test_user_random_number(self):
        """User assigned random number should be between 1 and 100"""
        user_max = User.objects.get(email="max@masters.com")
        user_kid = User.objects.get(email="kid@masters.com")
        self.assertTrue(1 <= user_max.rnd_number <= 100)
        self.assertTrue(1 <= user_kid.rnd_number <= 100)

    def test_eligible(self):
        """User birthday should transform correctly using eligible template tag"""
        user_max = User.objects.get(email="max@masters.com")
        user_kid = User.objects.get(email="kid@masters.com")
        self.assertEqual(eligible(user_max.birthday), 'allowed')
        self.assertEqual(eligible(user_kid.birthday), 'blocked')

    def test_bizzfuzz(self):
        """User random number should transform correctly using bizzfuzz template tag"""
        user_max = User.objects.get(email="max@masters.com")
        user_max.rnd_number = 9                     # Multiple of 3
        self.assertEqual(bizzfuzz(user_max.rnd_number), 'Bizz')
        user_max.rnd_number = 50                    # Multiple of 5
        self.assertEqual(bizzfuzz(user_max.rnd_number), 'Fuzz')
        user_max.rnd_number = 45                    # Multiple of both 3 and 5
        self.assertEqual(bizzfuzz(user_max.rnd_number), 'BizzFuzz')
        user_max.rnd_number = 22                    # Not a multiple of 3 or 5
        self.assertEqual(bizzfuzz(user_max.rnd_number), user_max.rnd_number)
