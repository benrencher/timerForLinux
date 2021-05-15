class TimeTracker:
    def __init__(self, seconds, minutes, hours):
        if seconds is None:
            self.seconds = 0
        else:
            self.seconds = seconds
        if minutes is None:
            self.minutes = 0
        else:
            self.minutes = minutes
        if hours is None:
            self.hours = 0
        else:
            self.hours = hours