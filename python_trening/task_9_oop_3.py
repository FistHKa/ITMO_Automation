class Soda:

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}')

        else:
            print('Обычная газировка')

dobavka = Soda('Лимон')
not_dobavka = Soda()

dobavka.show_my_drink()
not_dobavka.show_my_drink()