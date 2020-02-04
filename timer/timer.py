
# timer class 

class myTimer:
    # constructor
    def __init__(self, startTime, targetTime):
        self.targetTime = targetTime
        self.counterValue = startTime

    # method count up
    def countUp(self):
        if self.counterValue < self.targetTime:

            self.counterValue = self.counterValue + 1
            return self.counterValue

        else:
            return None


# create the myTimer obj
timer1 = myTimer(10, 100)
timer2 = myTimer(20, 50)

while True:
    time1 = timer1.countUp()
    time2 = timer2.countUp()

    if time1 is None and time2 is None:
        break

    if time1 is not None:
        print("time1", time1)

    if time2 is not None:
        print("time2", time2)
