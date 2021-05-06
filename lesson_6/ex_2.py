import time

class Road:
    def __init__(self,width,length):
        self.__length = width
        self.__width = length


    def mass(self):
        self.mass = self.__length*self.__width*25*5
        print (f'{self.mass} т')

massa = Road(width=10,length=20)
massa.mass()

