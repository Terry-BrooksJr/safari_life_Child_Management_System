from pytz import common_timezones
import pickle
import datetime

class Student:
    def __init__(self, first_name, last_name, age, guardian, pay_method, exit_date=None, enrollment_date, days_missed=0, days_present=0, is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.guardian = Guardian(
            'Berlinda Maxwell', '7082286900', 'bmaxwell63@yahoo.com')
        self._days_missed = days_missed
        self._days_present = days_present
        self.enrollment_date = enrollment_date
        self.exit_date  = exit_date
        self.is_active = is_active
        self.pay_method = Account()
        # self.is_archive =is_active
        

    def present_attendance(self):
        self._days_present += 1
        return self

    def absent_attendence(self):
        self._days_present += 1
        return self

    def correct_attendance(self,present=0,absent=0):
        input(f"Do You Wish to Change The Number of Days {self.first_name} was marked in attendance?")
        if input in ['yes','Y','YES',True,'true','TRUE']:
            function_days = input(f"How days do want to add to the {self.first_name}'s attendance?(Use Negative values if removing days)")
            if function_days > 0:
                _days_present += function_days
                print(f'This student now has a total of {_days_present} days in attendance.')
            else: 
                _days_present -= abs(function_days)
                _days_missed += abs(function_days)
                print(f"You have added {abs(function_days)} to the student's absences")
        return self


class Guardian:
    def __init__(self, name, contact_phone, contact_email):
        self.name = name
        self.contact_phone=contact_phone
        self.contact_email=contact_email

#     def sleep(self):
#         self.Health.energy += 50
#         return self

#     def eat(self):
#         if self.Health.hunger < 10:
#             self.Health.anger += 5
#         else:
#             self.Health.hunger -= 20
#         return self

#     def play(self):
#         if self.Health.energy < 15:
#             self.Health.anger += 5
#         else:
#             self.Health.lonliness -= 10
#             self.Health.boredom -= 25
#             self.Health.energy - 15

#     def noise(self):
#         pass


class Account:
    def _init__(self, energy=50, hunger=50, boredom=25, lonliness=25, anger=0):
        self.energy = energy
        self.hunger = hunger
        self.boredom = boredom
        self.anger = anger
        self.lonliness = lonliness


# class Bird(Pet):
#     def __init__(self, name, type, tricks, wing_span, flight):
#         super().__init__(name, type, tricks)
#         self.name = name
#         self.type = type
#         self.wing_span = wing_span
#         self.flight = flight

#     def fly(self):
#         if self.Health.energy < 15:
#             self.Health.anger += 5
#         else:
#             self.Health.energy - 15


# class Dog(Pet):
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)


# class Cat(Pet):
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)
    
guardian_test = Guardian('Berlinda Maxwell','7082286900','bmaxwell63@yahoo.com')
account_test = Account()
test=Student('Terry', 'Brooks', 33,guardian_test,account_test)
