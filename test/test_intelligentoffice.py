import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError



class TestIntelligentOffice(unittest.TestCase):
    @patch.object(GPIO, "input")
    def test_check_occupancy_all_pins_different_states(self, mock_sensor: Mock):
        office = IntelligentOffice()
        # Provide a list of results in the order they will be called
        mock_sensor.side_effect = [True, True, False, True]
        res1 = office.check_quadrant_occupancy(office.INFRARED_PIN1)
        res2 = office.check_quadrant_occupancy(office.INFRARED_PIN2)
        res3 = office.check_quadrant_occupancy(office.INFRARED_PIN3)
        res4 = office.check_quadrant_occupancy(office.INFRARED_PIN4)
        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertFalse(res3)
        self.assertTrue(res4)
        # Verify hardware was hit exactly 4 times
        self.assertEqual(mock_sensor.call_count, 4)

    @patch.object(GPIO, "input")
    def test_detect_worker_in_office_by_specific_pin(self, mock_sensor: Mock):
        office = IntelligentOffice()
        # Define how the hardware should respond to specific pins
        def side_effect_func(pin):
            return pin == office.INFRARED_PIN1 # True only for PIN3, False for others
        # Assign the function to side_effect (not return_value)
        mock_sensor.side_effect = side_effect_func
        # Execution: Check different pins
        test_sensor2 = office.check_quadrant_occupancy(office.INFRARED_PIN2)
        test_sensor1 = office.check_quadrant_occupancy(office.INFRARED_PIN1)
        test_sensor4 = office.check_quadrant_occupancy(office.INFRARED_PIN4)

        # Assertions
        self.assertFalse(test_sensor2, "Pin 2 should be empty")
        self.assertTrue(test_sensor1, "Pin 1 should be occupied")
        self.assertFalse(test_sensor4, "Pin 4 should be empty")

        # We called the method 3 times total
        self.assertEqual(mock_sensor.call_count, 3)
    def test_check_occupancy_raise_error_2(self):
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

    @patch.object(GPIO, "output")
    @patch.object(GPIO, "input")
    def test_monitor_air_quality_detect_smoke(self, mock_smoke_sensor: Mock, mock_buzzer: Mock):
        office = IntelligentOffice()
        mock_smoke_sensor.return_value = False
        mock_buzzer.return_value = True
        office.monitor_air_quality()
        self.assertTrue(office.buzzer_on)
        mock_smoke_sensor.assert_called_with(office.GAS_PIN)
        mock_buzzer.assert_called_with(office.BUZZER_PIN, True)


    @patch.object(GPIO, "output")
    @patch.object(GPIO, "input")
    def test_monitor_air_quality_no_smoke(self, mock_smoke_sensor: Mock, mock_buzzer: Mock):
        office = IntelligentOffice()
        mock_smoke_sensor.return_value = True
        mock_buzzer.return_value = False
        office.monitor_air_quality()
        self.assertFalse(office.buzzer_on)
        mock_smoke_sensor.assert_called_with(office.GAS_PIN)
        mock_buzzer.assert_called_with(office.BUZZER_PIN, False)






