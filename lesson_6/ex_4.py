
class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        if self.is_police is True:
            self.n = 'это полиция'
        else:
            self.n = 'это не полиция'


    def go(self):
        print('Going')

    def stop(self):
        print('Stopping')

    def turn(self,direction):
        print(f'Car is turn to the {direction}')

    def show_speed(self):
        return self.speed

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена {self.speed}')
        else:
            print(f'Скорость в порядке {self.speed}')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
             print(f'Скорость превышена {self.speed}')
        else:
            print(f'Скорость в порядке {self.speed}')

class PoliceCar(Car):
    pass


a = WorkCar(speed=30,color='красный',name='Lada',is_police=False)
print (f'Со скоростью {a.speed} км/ч, движется автомобиль {a.name} , {a.color} цвет, {a.n}')
print (a.show_speed())
#print (a.go())

a = TownCar(speed=80,color='синий',name='Pego',is_police=True)
print (f'Со скоростью {a.speed} км/ч, движется автомобиль {a.name} , {a.color} цвет, {a.n}')
b = a.show_speed()
#print (b)