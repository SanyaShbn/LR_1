class Match:
    counter = 0
    def __init__(self, date, time, weekday):
        self.date = date
        self.time = time
        self.weekday = weekday
        Match.counter += 1
    def show_info(self):
        print("Дата матча команды - " + self.date + " время - " + self.time + " день недели  - " + self.weekday)

    @classmethod
    def count_matches(cls):
        print("Количество матчей в календаре - " + str(cls.counter))
    @staticmethod
    def show_result(check):
        if(check):
            print("Прогноз - победа")
        else:
            print("Прогноз - поражение")

match1 = Match("02.11.2023", "19.30", "Четверг")
match2 = Match("04.11.2023", "14.00", "Суббота")
match3 = Match("06.11.2023", "19.00", "Понедельник")
match1.show_info()
match1.show_result(True)
match2.show_info()
match2.show_result(False)
match3.show_info()
match3.show_result(True)
match2.count_matches()
