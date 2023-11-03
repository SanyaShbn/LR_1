class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
class Position(Worker):
    def get_full_name(self):
        full_name = "Полное имя работника - " + str(self.surname) + " " + str(self.name)
        print(full_name)
    def get_total_income(self):
        total_income = int(self._income["wage"]) + int(self._income["bonus"])
        print("Доход работника с учётом премии - " + str(total_income))

worker1 = Position("Александр", "Смирнов", "Босс",{"wage": 1000000, "bonus": 20000})
worker2 = Position("Иван", "Иванов", "Небосс",{"wage": 50000, "bonus": 5000})
worker1.get_full_name()
worker2.get_full_name()
worker1.get_total_income()
worker2.get_total_income()
