import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError


class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_detect_worker_in_quadrant_1(self, infrared_sensor_1: Mock):
        infrared_sensor_1.return_value = True
        office = IntelligentOffice()
        self.assertTrue(office.check_quadrant_occupancy(office.INFRARED_PIN1))

    @patch.object(GPIO, "input")
    def test_detect_worker_in_office(self, infrared_distance_sensor: Mock):
        infrared_distance_sensor.return_value = True
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN2)
        self.assertTrue(outcome)
    def test_check_occupancy_raise_error(self):
        office = IntelligentOffice()
        self.assertRaises(IntelligentOfficeError, office.check_quadrant_occupancy, 1)

    @patch.object(SDL_DS3231, "read_datetime")
    def test_manage_blinds_based_on_time(self, mock_datetime: Mock):
        mock_datetime.return_value = {"hour": 12, "minute": 0, "second": 0}
        office = IntelligentOffice()
        office.manage_blinds_based_on_time()
        self.assertTrue(office.blinds_open)



