class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen():
    def draw(self):
        print("Вы используете ручку для отрисовки")
class Pencil():
    def draw(self):
        print("Вы используете карандаш для отрисовки")
class Handle():
    def draw(self):
        print("Вы используете маркер для отрисовки")

stationary = Stationery("Название")
stationary.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
