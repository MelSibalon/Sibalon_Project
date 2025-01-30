from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class UserRegistrationTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'password1': 'Testpassword123!',
            'password2': 'Testpassword123!',
            'role': 'player',
            'age': 25,
            'phone_number': '1234567890'
        }

    def test_user_registration(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
      

    def test_registration_invalid_username(self):
        self.valid_data['username'] = ''  # Invalid username
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertEqual(response.status_code, 200)  # Should return to the signup page
        self.assertFormError(response.context['form'], 'username', 'This field is required.')


    def test_registration_existing_username(self):
        self.client.post(reverse('signup'), self.valid_data)  # Create the user first
        response = self.client.post(reverse('signup'), self.valid_data)  # Try to create again
        self.assertEqual(response.status_code, 200)  # Should return to the signup page
        self.assertFormError(response.context['form'], 'username', 'A user with that username already exists.')
    def test_user_registration(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
      

    def test_registration_invalid_username(self):
        self.valid_data['username'] = ''  # Invalid username
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertEqual(response.status_code, 200)  # Should return to the signup page
        self.assertFormError(response, 'form', 'username', 'This field is required.')

    def test_registration_existing_username(self):
        self.client.post(reverse('signup'), self.valid_data)  # Create the user first
        response = self.client.post(reverse('signup'), self.valid_data)  # Try to create again
        self.assertEqual(response.status_code, 200)  # Should return to the signup page
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')

class UserLoginTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='Testpassword123!')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Testpassword123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Should return to the login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class UserProfileTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='Testpassword123!')
   
    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.role, 'player')
        self.assertEqual(self.user_profile.user.username, 'testuser')
