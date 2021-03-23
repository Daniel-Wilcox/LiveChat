from django.test import TestCase
# from django.core.urlresolvers import reverse
# from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import get_user_model
import datetime
# Create your tests here.


# class CreateAccountTest(TestCase):
#     def test_new_superuser():
#         db = get_user_model()
#         super_user = db.objects.create_superuser(
#             'super', 'super@user.com', datetime.datetime(1990, 1, 1), 'password')

#         self.assertEqual(super_user.username, 'super')
#         self.assertEqual(super_user.email, 'super@user.com')
#         self.assertEqual(super_user.date_of_birth,
#                          datetime.datetime(1990, 1, 1))
#         self.assertTrue(super_user.is_superuser)
#         self.assertTrue(super_user.is_staff)
#         self.assertTrue(super_user.is_active)
#         self.assertEqual(str(super_user), 'super')
#         self.assertEqual(super_user.get_profile_url(), "/users/super/")

#         with self.assertRaise(ValueError):
#             db.objects.create_superuser(
#                 username='super', email='super@user.com',
#                 date_of_birth=datetime.datetime(1990, 1, 1), password='password',
#                 is_superuser=False
#             )

#         with self.assertRaise(ValueError):
#             db.objects.create_superuser(
#                 username='', email='super@user.com',
#                 date_of_birth=datetime.datetime(1990, 1, 1), password='password',
#                 is_superuser=True
#             )

#         with self.assertRaise(ValueError):
#             db.objects.create_superuser(
#                 username='super', email='',
#                 date_of_birth=datetime.datetime(1990, 1, 1), password='password',
#                 is_superuser=True
#             )

#         with self.assertRaise(ValueError):
#             db.objects.create_superuser(
#                 username='super', email='super@user.com',
#                 date_of_birth='1999-01-01', password='password',
#                 is_superuser=True
#             )

#     def test_new_user():

#         db = get_user_model()
#         user = db.objects.create_superuser(
#             'user1', 'user1@user.com', datetime.datetime(1990, 1, 1), 'password')

#         self.assertEqual(user.username, 'user')
#         self.assertEqual(user.email, 'user1@user.com')
#         self.assertEqual(user.date_of_birth,
#                          datetime.datetime(1990, 1, 1))
#         self.assertFalse(user.is_superuser)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_active)
#         self.assertEqual(str(user), 'user1')
#         self.assertEqual(user.get_profile_url(), "/users/user1/")

#         with self.assertRaise(ValueError):
#             db.objects.create_user(
#                 username='', email='user1@user.com',
#                 date_of_birth=datetime.datetime(1990, 1, 1), password='password')

#         with self.assertRaise(ValueError):
#             db.objects.create_user(
#                 username='user1', email='',
#                 date_of_birth=datetime.datetime(1990, 1, 1), password='password')

#         with self.assertRaise(ValueError):
#             db.objects.create_user(
#                 username='user1', email='user1@user.com',
#                 date_of_birth='1999-01-01', password='password')

# class AccountsTest(APITestCase):
#     def setUp(self):
#         # We want to go ahead and originally create a user.
#         today = date.today()
#         self.test_user = User.objects.create_user(
#             'testuser', 'test@example.com', 'testpassword')

#         # URL for creating an account.
#         self.create_url = reverse('account-create')

#     def test_create_user(self):
#         """
#         Ensure we can create a new user and a valid token is created with it.
#         """
#         data = {
#             'username': 'foobar',
#             'email': 'foobar@example.com',
#             'password': 'somepassword'
#         }

#         response = self.client.post(self.create_url, data, format='json')

#         # We want to make sure we have two users in the database..
#         self.assertEqual(User.objects.count(), 2)
#         # And that we're returning a 201 created code.
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # Additionally, we want to return the username and email upon successful creation.
#         self.assertEqual(response.data['username'], data['username'])
#         self.assertEqual(response.data['email'], data['email'])
#         self.assertFalse('password' in response.data)
