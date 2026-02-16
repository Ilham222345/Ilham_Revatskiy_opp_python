"""""
======================================
1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому.
======================================
Решение:
"""""
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age
    def get_data(self):
        return (f"Имя: {self.name}, Возраст: {self.age}")
a = Person()
b = Person()
a.name = "Liam"
b.name = "Jim"
a.age = 20
b.age = 29
print(a.get_data())
print(b.get_data())
"""""
======================================
2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
======================================
3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords().
Решение:
"""""
class Point:
    def set_coords(self, coorsds:tuple):
        self.coords = coorsds
    def get_coords(self):
        return self.coords
p = Point()
p.set_coords((7, 12))
print(p.get_coords())
p.set_coords((-3, 5))
print(p.get_coords())

print(getattr(p, 'get_coords')())
"""""
======================================
4. Создай класс Person, в котором метод init() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
======================================
5. Добавь в класс Person метод del(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
======================================
Решение:
==========================
"""""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")
    def __del__(self):
        print(f"Удален объект: {self.name}")

obj = Person("Bob", 89)
obj.show_info()
obj_2 = Person("Arsen", 123)
del obj_2
"""""
======================================
6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
======================================
Решение:
"""
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
obj = Rectangle()
print(obj.area())
"""""
======================================
7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в new выводи Создание логгера,
а при вызове init — Инициализация логгера.
======================================
Решение:
"""
class Logger:
    instance = None
    def __new__(cls, *args, **kwargs):
        print("Создание логгера")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        print("Инициализация логгера")
obj = Logger()