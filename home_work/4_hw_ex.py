class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def star(self):
        print('Автомобиль заведен')

    def end(self):
        print('Автомобиль заглушен')

    def years(self, new_year):
        self.years = new_year
        print('Новый год =', self.years)

    def types(self, new_type):
        self.types = new_type
        print('Новый тип =', self.types)

    def colors(self, new_color):
        self.colors = new_color
        print('Новый цвет =', self.colors)

car_1 = Car('Green', 'Minivan', '2008')
car_1.star()
car_1.end()
print(car_1.year)
print(car_1.color)
print(car_1.type)
car_1.years('2020')
car_1.colors('Red')
car_1.types('Sedan')