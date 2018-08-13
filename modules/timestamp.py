"""Class to append Timestamp to other objects


"""
import datetime


class TimeStamp:
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def print_dates(self):
        print(self.created_at)
