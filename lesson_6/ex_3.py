
class Worker:
    def __init__(self,name,surname,position,income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": income, "bonus": 1500}

class Position(Worker):

    def get_full_name(self):
        print(self.name,self.surname)

    def get_total_income(self):
        total_income = 0
        total_income = self._income["wage"] + self._income["bonus"]
        print(f'{total_income} Р')

Pos = Position(name='Kris',surname='Berdos',position='Loader',income=1000)
Pos.get_full_name()
Pos.get_total_income()
