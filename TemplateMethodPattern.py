from abc import ABC, abstractmethod

class Drink(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_extras()

    def boil_water(self):
        print("\tКип'ятимо воду")

    def pour_in_cup(self):
        print("\tНаливаємо в чашку")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass


class Coffee(Drink):
    def brew(self):
        print("\tЗаварюємо каву")

    def add_extras(self):
        print("\tДодаємо молоко і цукор")


class Tea(Drink):
    def brew(self):
        print("\tЗаварюємо чайний пакетик")

    def add_extras(self):
        print("\tДодаємо лимон")


class Compote(Drink):
    def brew(self):
        print("\tВаримо фрукти")

    def add_extras(self):
        print("\tДодаємо цукор")


coffee = Coffee()
print("Готуємо каву")
coffee.prepare()

tea = Tea()
print("Готуємо чай")
tea.prepare()

compote = Compote()
print("Готуємо компот")
compote.prepare()