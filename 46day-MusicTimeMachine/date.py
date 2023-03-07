import re
from datetime import datetime, date

class DateValidator:
    
    def __init__(self, date_input: str) -> None:
        self.date_input = date_input
        self.year_input = int(self.date_input.split("-")[0])
        self.month_input = int(self.date_input.split("-")[1])
        self.day_input= int(self.date_input.split("-")[2])
        self.today = datetime.now().date()
        self.current_date = datetime.strptime(str(self.today), "%Y-%m-%d")
        self.past_date = datetime(1958, 8, 4)
        
    def _datelimit_past_error(self):
        """ Return ab error string about the date is older than first bilboard chart"""
        return f"The {self.date_input} is out of the billboard top chart range, please choose a year equal or greater than 1958-08-04 until {self.today}"
    
    def _datelimit_future_error(self):
        """ Return an error string about the date being in the future"""
        return f"The {self.date_input} is out of the billboard top chart range, please choose a year equal or less than {self.today}"
    
    def _check_datelimit(self):
        """ Check the datelimit for the date user input"""
        self.date_input_datetime = datetime.strptime(self.date_input, "%Y-%m-%d")
        if self.date_input_datetime < self.past_date:
            raise Exception(self._datelimit_past_error())
        elif self.date_input_datetime > self.current_date:
            raise Exception(self._datelimit_future_error())
        else:
            return True
        
    def _check_month(self):
        """ Check if the date user input has a valid month"""
        if self.month_input < 1 or self.month_input > 12:
            raise Exception(f"!!! {self.month_input} is not a valid Month, allowed range from 1 to 12")
        else:
            return True
    
    def _check_day(self):
        """ Check if the date user input has a valid day"""
        if self.day_input < 1 or self.day_input > 31:
            raise Exception(f"!!! {self.day_input} is not a valid Day, allowed range from 1 to 31")
        else:
            return True
            
    def check_fulldate(self):
        """ Check if the date user input has a valid format, month, day and if don't exceed the limit dates"""
        if re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', self.date_input):
            if self._check_datelimit():
                    if self._check_month:
                        if self._check_day:
                            return self.date_input
        else:
            raise Exception(f"!!! {self.date_input} is an invalid date Type the date in the format YYYY-MM-DD")
        