from django.test import TestCase
from .models import neighbourhood, healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.


class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.nairobi = neighbourhood(neighbourhood='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Kahawa.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.nairobi.delete_neighbourhood('nairobi')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)


class healthservicesTestClass(TestCase):
    def setUp(self):
        self.cardio = healthservices(healthservices='cardio')

    def test_instance(self):
        self.assertTrue(isinstance(self.cardio, healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Radiotherapy.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health) > 0)

    def test_delete_method(self):
        self.cardio.delete_healthservices('cardio')
        health = healthservices.objects.all()
        self.assertTrue(len(health) == 0)
