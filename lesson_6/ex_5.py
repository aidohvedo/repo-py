
class Stationery:
    def __init__(self,title):
        self.title = title


    def draw(self):
        print('Drawing')

class Pen(Stationery):

    def draw(self):
        print('Drawing pen')

class Pencil(Stationery):

    def draw(self):
        print('Drawing pencil')

class Marker(Stationery):

    def draw(self):
        print('Drawing marker')



a = Stationery('pen')
a.draw()
a = Pen('pen')
a.draw()