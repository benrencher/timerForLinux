import time

class TimeTracker:
    def __init__(self, seconds, minutes, hours):
        self.hours = hours
        self.minutes = minutes
        hoursAsSeconds = hours * 3600
        minutesAsSeconds = minutes * 60
        self.seconds = seconds + hoursAsSeconds + minutesAsSeconds

    def calculateTime(self):
        tempSeconds = self.seconds
        self.hours = tempSeconds // 3600
        tempSeconds %= 3600
        self.minutes = tempSeconds // 60
        tempSeconds %= 60

    def display(self):
        #for now just log the seconds in the console
        print(self.seconds)
        if self.seconds == 0:
            print("Times up!")

    def decrementSeconds(self):
        self.seconds -= 1
        self.calculateTime()

    def incrementSeconds(self):
        self.seconds += 1
        self.calculateTime()

    def startTimer(self):
        while self.seconds > 0:
            time.sleep(1)
            self.decrementSeconds()
            self.display()

    def startStopWatch(self):
        while True:
            time.sleep(1)
            self.incrementSeconds()
            self.display()