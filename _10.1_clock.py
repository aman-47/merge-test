

# C# clock program in Python.
# Created by Aman

import time


class Counter:
    #Counter class.
    def __init__(self):
        self.count = 0

    def increment(self):
        #Increment Counter.
        self.count += 1

    def reset(self):
        #Reset Counter.
        self.count = 0


class Clock(Counter):
    #Clock class.
    def __init__(self, hours=0, mins=0, secs=0):
        Counter.__init__(self)
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def time(self):
        #Return hh:mm:ss count.
        self.hours = self.count // 3600
        self.mins = self.count // 60 % 60
        self.secs = self.count % 60

        return f"{self.hours:02d}:{self.mins:02d}:{self.secs:02d}"


def main():
    #Main function.
    clock = Clock()

    while True:
        clock.increment()
        print(clock.time(), end="\r")
        time.sleep(1)


if __name__ == "__main__":
    main()

