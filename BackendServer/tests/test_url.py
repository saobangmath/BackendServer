from django.urls import resolve, reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'newuser',
            'password': 'newpassword'}
        User.objects.create_user(**self.credentials)


    def test_login_newuser(self):
        # login
        print('\ntesting login newuser')
        response = self.client.post('/login/', {'username':'newuser', 'password':'newpassword'}, follow=True)
        # print('response',response.context['user'])
        # should be logged in now, fails however
        assert response.context['user'].is_authenticated   # account just created, assert True


    def test_login_wrongpassword(self):
        # login
        print('\ntesting login wrongpassword')
        response = self.client.post('/login/', {'username':'newuser', 'password':'oldpassword'}, follow=True)
        # print('response',response.context['user'])
        # should be logged in now, fails however
        assert not response.context['user'].is_authenticated   # account just created, assert True


    def test_login_fake(self):
        # login
        print('\ntesting login fake')
        response = self.client.post('/login/', {'username':'fake', 'password':'fake'}, follow=True)
        # print('response fake',response)
        # should be logged in now, fails however
        assert not response.context['user'].is_authenticated   # account does not exist, assert not


class TestUrls(TestCase):

    def test_login_url(self):
        path = reverse('login', kwargs={})
        assert resolve(path).view_name == 'login'
        print('\ntesting login')

    def test_fake_url(self):
        print('\ntesting fake')
        try:
            path = reverse('fake', kwargs={})   # url does not exist

        except NoReverseMatch:
            print('caught no reverse match')
            assert True
        except:
            print('test fake fail')
            assert False

    def test_levels_url(self):
        path = reverse('levels', kwargs={})
        assert not resolve(path).view_name == 'level'   # typo on purpose, should not match, asserting not
        print('\ntesting levels')

    def test_logout_url(self):
        path = reverse('logout', kwargs={})
        assert resolve(path).view_name == 'logout'
        print('\ntesting logout')


    def test_home_url(self):
        path = reverse('home', kwargs={})
        assert resolve(path).view_name == 'home'
        print('\ntesting home')


    def test_register_url(self):
        path = reverse('register', kwargs={})
        assert resolve(path).view_name == 'register'
        print('\ntesting register')


    def test_questions_url(self):
        path = reverse('questions', kwargs={})
        assert resolve(path).view_name == 'questions'
        print('\ntesting questions')




