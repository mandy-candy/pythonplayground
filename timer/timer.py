
# timer class 

class myTimer:
    # constructor
    def __init__(self, startTime, targetTime):
        # set function parameters to member variables self.
        self.targetTime = targetTime
        self.counterValue = startTime

    # method count up
    def countUp(self):
        if self.counterValue < self.targetTime:

            # short self.counterValue += 1
            self.counterValue = self.counterValue + 1
            # return the self.counterValue to function caller
            return self.counterValue

        else:
            # None is a specific word in python
            return None


# create the myTimer obj (can create as many as we want)
timer1 = myTimer(10, 100)
timer2 = myTimer(20, 50)

while True:
    # set return of countUp() to time1 / time2
    time1 = timer1.countUp()
    time2 = timer2.countUp()

    # if time 1 and time2 is None stop program
    if time1 is None and time2 is None:
        break

    # as long as time is not None print
    if time1 is not None:
        print("Time 1", time1)

    if time2 is not None:
        print("Time 2", time2)
