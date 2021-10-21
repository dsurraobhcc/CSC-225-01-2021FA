from datetime import datetime

class Meeting:

    def __init__(self, name, scheduled_time, priority=0):
        self.name = name
        self.scheduled_time = scheduled_time

    def __str__(self):
        return f'{self.name}: {self.scheduled_time}'

    def __lt__(self, other):
        return self.scheduled_time < other.scheduled_time


if __name__ == '__main__':
    dr_appt = Meeting('Doctor\'s appt', datetime(2021, 10, 22, 9))
    dentist_appt = Meeting('Dentist appt', datetime(2021, 10, 22, 10))
    python_class = Meeting('Python class', datetime(2021, 11, 1, 8, 30))

    # print(dr_appt > dentist_appt)
    # print(dentist_appt < dr_appt)

    meetings = [dentist_appt, python_class, dr_appt]
    meetings.sort(reverse=True)

    for meeting in meetings:
        print(meeting)
