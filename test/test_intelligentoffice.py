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

    @patch.object(IntelligentOffice, "change_servo_angle")
    @patch.object(SDL_DS3231, "read_datetime")
    def test_manage_blinds_based_on_time(self, mock_current_time: Mock, servo_moto: Mock):
        mock_current_time.return_value = datetime(2025, 12, 19, 12, 0, 0)
        office = IntelligentOffice()
        office.manage_blinds_based_on_time()
        servo_moto.assert_called_with(12)
        self.assertTrue(office.blinds_open)

    '''@patch.object(GPIO, "output")
    @patch.object(VEML7700, "lux", new_callable=PropertyMock)
    def test_manage_light_level(self, mock_lux:Mock, mock_led: Mock):
        mock_lux.return_value= 490
        office = IntelligentOffice()
        office.manage_light_level()
        #self.assertTrue(office.light_on)
        mock_led.assert_called_with(office.LED_PIN, True)'''

    @patch.object(IntelligentOffice, "check_quadrant_occupancy")
    @patch.object(GPIO, "output")
    @patch.object(VEML7700, "lux", new_callable=PropertyMock)
    def test_manage_light_level_based_on_occupancy(self, mock_lux:Mock, mock_led: Mock, mock_infrared:Mock):
        mock_lux.return_value= 100
        mock_infrared.return_value = False
        office = IntelligentOffice()
        office.manage_light_level()
        self.assertFalse(office.light_on)
        mock_led.assert_called_with(office.LED_PIN, False)







