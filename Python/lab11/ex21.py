import math
class Calculator:
    def __init__(self, acc = 0.00): 
        self.acc = acc
    def set_accumulator(self, a):
        self.acc = a
    def get_accumulator(self):
        return self.acc
    def add(self, x):
        self.acc += x
    def subtract(self, x):
        self.acc -= x
    def multiply(self, x):
        self.acc *= x
    def divide(self, x):
        if x == 0:
            print("Undefined")
        else:
            self.acc /= x
            self.print_result()
    def print_result(self):
        print(f"Result: {self.get_accumulator()}")
class Sci_calc(Calculator):
    def __init__(self, acc):
        super().__init__(acc)
    def square (self):
        self.acc = self.acc * self.acc
    def exp(self, x):
        self.acc = self.acc**x
    def factorial(self):
        self.acc = math.factorial(int(self.acc))
    def print_result(self):
        print(f"Result: {self.acc:.1e}")
acc = Calculator(10.0)
acc.add(20)
acc.subtract(10)
acc.multiply(2)
acc.divide(4)

sci_calc = Sci_calc(100.0)
sci_calc.print_result()

