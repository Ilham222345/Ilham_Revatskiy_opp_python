"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================
"""
import time

class Cat:
    def speak(self):
        print("Класс кошка")

class Dog:
    def speak(self):
        print("Класс собака")

class Duck:
    def speak(self):
        print("Класс утка")

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    animal.speak()

"""
======================================
2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================
"""

class Shape:
    def ger_pr(self):
        print('Shape')

class Square(Shape):
    def ger_pr(self):
        print('Square')
        super().ger_pr()

class Rectangle(Shape):
    def ger_pr(self):
        print('Rectangle')
        super().ger_pr()

class Triangle(Shape):
    def ger_pr(self):
        print('Triangle')
        super().ger_pr()

shapes = [Square(), Rectangle(), Triangle()]
for shape in shapes:
    shape.ger_pr()

"""
======================================
3. Сделай класс Shape абстрактным.
Переопредели get_pr() как @abstractmethod.
Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
======================================
"""

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def ger_pr(self):
        print('Shape')

class Square(Shape):
    def __init__(self):
        print('Square')

shapes = Square()

"""
======================================
4. Создай классы A, B, C, в каждом — свой init() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().init() в каждом init.
Выведи D.mro и посмотри, в каком порядке вызываются инициализаторы.
======================================
"""

class A:
    def __init__(self):
        print("init A")
        super().__init__()
class B:
    def __init__(self):
        print("init B")
        super().__init__()
class C:
    def __init__(self):
        print("init C")
class D(A, B, C):
    def __init__(self):
        print("init D")
print(D.__mro__)

"""
5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================
"""

class Goods:
    def __init__(self, name, data, deposit):
        super().__init__()
        self.name = name
        self.data = data
        self.deposit = deposit

    def print_info(self):
        if self.deposit:
            print(f"Ваше имя: {self.name}\n"
                  f"Дата бронирования: {self.data}\n"
                  f"Депозит внесен.")

class MixinLog:
    def __init__(self):
        print("Бронирование гостинницы...")
        time.sleep(4)
        print("Бронь прошла успешно.")
    def print_info(self):
        print("Реализуюю пробный сервис")

# class Notebook(Goods, MixinLog):
#     pass

class Notebook(MixinLog, Goods):
    pass

n = Notebook("Bob", "23.02", "True")
n.print_info()
# Логика изменилась, ничего теперь не работает...

"""
======================================
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
======================================
"""

firt_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
if second_number == 0:
    raise ZeroDivisionError ("На ноль делить нельзя!")
else: print(f"Деление первого числа, на второе: {firt_number // second_number}")

"""
======================================
8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================
"""
firt_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    result =float(firt_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")

""" 
======================================
9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================
"""

firt_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    result =float(firt_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа через пробел")
except Exception:
    print("Произошла неизвестная ошибка")

"""   
======================================
10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================
"""

firt_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    result =float(firt_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
    e = 'ZeroDivisionError'
    print(e)
except ValueError:
    e = 'ValueError'
    print(e)
    print("Ошибка ввода: введите два числа через пробел")
except Exception:
    e = 'Exception'
    print(e)
    print("Произошла неизвестная ошибка")

"""
======================================
11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================
"""
try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    z = input("Введите арифметическую операцию: ")
    if z == "*":
         print(x * y)
    elif z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    elif z == "/":
        print(x / y)
    elif z == "**":
        print(x ** y)
    elif z == "//":
        print(x // y)
    else:
        z == "%"
        print(x % y)
except ArithmeticError:
    print("На ноль делить нельзя")
except ValueError:
    print("Неправильное значение")


"""
======================================
12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================
"""

firt_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    result = float(firt_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
    e = 'ZeroDivisionError'
    print(e)
except ValueError:
    e = 'ValueError'
    print(e)
    print("Ошибка ввода: строку вводить нельзя")
except Exception:
    e = 'Exception'
    print(e)
    print("Произошла неизвестная ошибка")
else:
    print("Деление прошло успешно")

"""
======================================
13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.
======================================
"""

firt_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    result = float(firt_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
    e = 'ZeroDivisionError'
    print(e)
except ValueError:
    e = 'ValueError'
    print(e)
    print("Ошибка ввода: строку вводить нельзя")
except Exception:
    e = 'Exception'
    print(e)
    print("Произошла неизвестная ошибка")
finally:
    print("Работа программы завершена")

"""
======================================
14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================
"""
first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    first_number = float(first_number)
    second_number = float(second_number)
    try:
        result = first_number / second_number
        print("Результат: ", result)
    except ZeroDivisionError:
         print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода, нужно вводить число!")

"""
======================================
15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
"""
try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    def divide(x, y):
        try:
            result = x / y
            print("Результат: ", result)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
    divide(x, y)
except ValueError:
    print("Ошибка ввода, нужно вводить число!")