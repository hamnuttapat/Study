class Time:
    def __init__  (self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        


    def print(self):
        formatted_time = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        print(formatted_time + " Hrs.")

times = Time(9, 30, 0)
times.print()

