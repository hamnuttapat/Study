from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, startplace, endplace, distance) -> None:
        self.start_place = startplace
        self.end_place = endplace
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, startplace, endplace, distance) -> None:
        super().__init__(startplace, endplace, distance)
    
    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, startplace, endplace, distance) -> None:
        super().__init__(startplace, endplace, distance)
    def find_cost(self):
        return 40 * self.distance
    
class Train(Transportation):
    def __init__(self, startplace, endplace, distance, stations) -> None:
        super().__init__(startplace, endplace, distance)
        self.stations = stations
    def find_cost(self):
        return self.stations * 5
    
def main():
    w = Walk("KMITL", "Lawson", 0.6)
    tx1 = Taxi("Lawson", "Ladkrabang Station", 5)
    train = Train("Ladkrabang Station", "Payathai", 40, 6)
    tx2 = Taxi("Payathai Station", "The Britiish Council", 3)
    print(w.find_cost(),tx1.find_cost(),train.find_cost(), tx2.find_cost())

if __name__ == "__main__":
    main()