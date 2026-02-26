"""
======================================
1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
======================================
"""

def inner():
    print(15 / 0)

def outer():
    inner()

outer()

"""
======================================
2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне".
======================================
"""

def inner():
    print(15 / 0)

def outer():
    inner()
try:
    outer()
except ZeroDivisionError:
    print("Ошибка перехвачена на верхнем уровне")

"""
======================================
3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner".
======================================
"""

def inner():
    try:
        print(15 / 0)
    except ZeroDivisionError:
        print("Ошибка в inner")

def outer():
    inner()

outer()

"""
======================================
4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer".
======================================
"""

def inner():
    print(15 / 0)

def outer():
    try:
        inner()
    except ZeroDivisionError:
        print("Ошибка в outer")

outer()

"""
======================================
5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано.
======================================
"""

def get_value():
    raise ValueError

def test_get_value():
    try:
        get_value()
    except ValueError:
        print("ValueError")
        assert False

test_get_value()

"""
======================================
6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления.
======================================
"""

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Ошибка, деление на ноль!")
    else:
        return x / y

"""
======================================
7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except.
======================================
"""

import math
class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError
    else:
        print(math.sqrt(x))

try:
    sqrt(-78)
except NegativeNumberError:
    print("Ошибка, число не может быть отрицательным")

"""
======================================
8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError.
======================================
"""

class MathError(Exception):
    pass
class NegativeNumberError(MathError):
    pass
class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Деление на ноль!")
    print(x / y)

try:
    safe_divide(1, 0)
except MathError as e:
    print(f"Ошибка: {e}")

"""
======================================
9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа".
======================================
"""

import math
class NegativeNumberError(Exception):
    pass

def test_sqrt():
    try:
        math.sqrt(-4)
    except NegativeNumberError:
        assert False, "Нельзя брать корень из отрицательного числа"
test_sqrt()

"""
======================================
10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with.
======================================
"""

with open("sample.txt") as f:
    sample = f.read()
    print(sample)

"""
======================================
11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке.
======================================
"""

class BackupList:
    def __init__(self, base):
        self.base = base

    def __enter__(self):
        self.copy = self.base.copy()
        return self.base

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.base[:] = self.copy
        return False

lst = [1, 2, 3]
try:
    with BackupList(lst) as backup:
        backup.append(4)
        1 / 0
except:
    pass
print(backup)

"""
======================================
12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат.
"""

from datetime import datetime

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        print(f"Начало работы функции: {start}")
        result = self.func(*args, **kwargs)
        end = datetime.now()
        print(f"Конец работы функции: {end}")
        return result
@Timer
def test():
    print("Выполняется функция")
test()
