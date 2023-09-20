# task_1
class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        if self.length > 0 and self.width > 0:
            return self.length * self.width
        else:
            return 'Введите корректные значения сторон'

    def perimeter(self):
        if self.length > 0 and self.width > 0:
            return (self.length + self.width) * 2
        else:
            return 'Введите корректные значения сторон'

object_1 = Rectangle(3, 8)
print(object_1.area())
print(object_1.perimeter())
object_2 = Rectangle(0, 6)
print(object_2.area())
print(object_2.perimeter())
object_3 = Rectangle(100, -2)
print(object_3.area())
print(object_3.perimeter())


# task_2
class Math:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print('inf')

    def subtraction(self):
        print(self.a - self.b)

w_1 = Math(-1, 10)
w_1.addition()

w_2 = Math(-8, -4)
w_2.multiplication()

w_3 = Math(10, 0)
w_3.division()

w_4 = Math(4, 7)
w_4.subtraction()


# task_3
class Button:

    def __init__(self, text, type, loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f"Клик по кнопке {self.text}")

b_1 = Button('Text box', 'button')
print(b_1.text)
b_1.click()
b_2 = Button('Check box', 'button')
print(b_2.text)
b_2.click()
b_3 = Button('Radio Button', 'button')
print(b_3.text)
b_3.click()
b_4 = Button('Web Tables', 'button')
print(b_4.text)
b_4.click()
b_5 = Button('Buttons', 'button')
print(b_5.text)
b_5.click()
b_6 = Button('Links', 'button')
print(b_6.text)
b_6.click()
b_7 = Button('Broken Links - Images', 'button')
print(b_7.text)
b_7.click()
b_8 = Button('Upload and Download', 'button')
print(b_8.text)
b_8.click()
b_9 = Button('Dynamic Properties', 'button')
print(b_9.text)
b_9.click()