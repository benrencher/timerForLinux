# Increase by one second
#   if the seconds is less than 60, keep going. else, divide by 60 and start at 00 and increase minutes by 1
#   If the minutes is less than 60, keep going. else, divide by 60 and start at 00 and increase hours by 1



class StopWatch:
    def __init__(self):
        self.currentTime = timeTracker.TimeTracker()

    def incrementTimer(self, currentTime):
        currentTime.seconds += 1
        self.checkRollOver(currentTime.seconds)
        hoursRollOver = self.checkRollOver(currentTime.minutes)
        currentTime.hours += hoursRollOver

    def checkRollOver(self, value):
        carryOver = 0
        if value == 60:
            value = 0
            carryOver = 1
        return carryOver