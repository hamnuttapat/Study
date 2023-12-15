class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def returna (self):
        return self.__a
    def returnb (self):
        return self.__b
    def returnc (self):
        return self.__c
    def getDiscriminant(self):
        return ((self.__b**2) - 4*(self.__a)*(self.__c))
    def r1 (self):
        if self.getDiscriminant() < 0:
            return 0 
        return ((-self.__b + ((self.__b**2) - 4*(self.__a)*(self.__c))**(1/2)) / (2*self.__a))
    def r2 (self):
        if self.getDiscriminant() < 0:
            return 0 
        return ((-self.__b - ((self.__b**2) - 4*(self.__a)*(self.__c))**(1/2)) / (2*self.__a))