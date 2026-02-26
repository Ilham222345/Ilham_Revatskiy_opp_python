"""
======================================
1. Создай класс Circle, в котором:
есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
Проверь результат вызова:
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False
======================================
2. Добавь в класс Circle:
статический метод area(radius),
который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
инициализацию в init, которая сохраняет радиус,
только если он проходит валидацию через метод is_valid_radius()
(подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
Пример:
c = Circle(10)
print(c.area(c.radius))  # Площадь круга
======================================
3. Расширь Circle, добавив обычный метод print_info, который выводит:
Радиус: ...
Допустимый диапазон: [MIN, MAX]
Метод должен использовать и self, и атрибуты класса через type(self).

Пример вызова:
c.print_info()
"""

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def __init__(self, radius):
        if Circle.is_valid_radius(radius):
            self.radius = radius

    @classmethod
    def is_valid_radius(cls, r: int):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        import math
        return math.pi * radius ** 2

    def print_info(self):
        print(f"Радиус: {self.radius}")
        print(f"Допустимый диапазон: [{self.MIN_RADIUS}, {self.MAX_RADIUS}]")

print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))
c = Circle(10)
print(c.area(c.radius))
c.print_info()
"""
======================================
4. Создай класс User, в котором:

приватные атрибуты login и password;
метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
метод get_credentials(), который возвращает кортеж из логина и пароля.
Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
======================================
5. Добавь в User:

метод check_password(password) — возвращает True,
если переданное значение совпадает с сохранённым паролем;
приватный метод __encrypt_password(password),
который возвращает пароль в верхнем регистре (имитация шифрования);
в set_credentials вызывай __encrypt_password.
Пример:
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False
======================================
6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
Попробуй это сделать — и поясни результат.
Также выведи напрямую u.__password — и проверь, что будет ошибка.

Попробуй добраться до данных через u._User__password
"""

class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def set_credentials(self, login: str, password: str):
        self.__login = login
        self.__password = password
        print(self.__encrypt_password(password))
    def get_credentials(self):
        return (self.__login, self.__password)
    def check_password(self, password):
        return self.__password == password
    def __encrypt_password(self, password):
        return password.upper()
tr = User("daniil", "qwerty")
print(tr.get_credentials())
tr.login = "daniil;lll"
print(tr.get_credentials())

tr.set_credentials("daniil;lll", "qwerty")
print(tr.check_password("qwerty"))
print(tr.check_password("qwe"))
print(tr.__encrypt_password())
print("Приватный метод спрятан, и не можем просто так его вызвать."
      "Он недоступен обычному пользователю.")

print(tr.__passwod)

print(tr._User__encrypt_password("ddddddddddd"))
