import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError


class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_if_infrared_sensor_1_detect_worker(self, infrared_sensor_1: Mock):
        infrared_sensor_1.return_value = True
        office = IntelligentOffice()
        self.assertTrue(office.check_quadrant_occupancy(office.INFRARED_PIN1))