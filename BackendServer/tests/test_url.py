from django.urls import resolve, reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch

class TestUrls(TestCase):

    def test_login_url(self):
        path = reverse('login', kwargs={})
        assert resolve(path).view_name == 'login'
        print('\ntesting login')


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

    def test_fake_url(self):
        print('\ntesting fake')
        try:
            path = reverse('fake', kwargs={})   # url does not exist
            resolve(path).view_name == 'fake'
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



