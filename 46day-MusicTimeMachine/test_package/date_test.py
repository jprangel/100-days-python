import unittest
from date import DateValidator

class TesteDate(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.valid_date = "1980-01-01"
        self.invalid_dates = ["1955-01-01", "2030-01-01", "1990-01-35", "1990-17-01", "12345-01-01", "1990-123-01", "2001-01-123"]
        
    def test_valid_date(self):
        """ Test the DateValidator class with a valid date"""
        self.date_validator = DateValidator(self.valid_date)
        self.assertAlmostEqual(self.date_validator.check_fulldate(), self.valid_date)
        
    def test_invalid_date(self):
        """ Test the DateValidator class with an invalid date"""
        for d in self.invalid_dates:
            with self.subTest(d=d):
                self.date_validator = DateValidator(d)
                with self.assertRaises(Exception):
                    result = self.date_validator.check_fulldate()