"""
======================================
1. Создай класс SecureData, который:

имеет атрибут secret, задаваемый в init__;
переопределяет getattribute, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"
======================================
2. Добавь в класс SecureData метод setattr,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает
======================================
"""

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def get_secret(self):
        return self.__secret

    def __setattr__(self, name, value):
        if name == "token":
            raise ValueError ("Такое имя нельзя использовать")
        object.__setattr__(self, name, value)

data = SecureData("пароль123")
# print(data.__secret)
print(data.get_secret())
# data.token = "abc123"
data.other = "ok"


"""
3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован getattr, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован delattr, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
======================================
"""

class SafeDict:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        return ("N/A")

    def __delattr__(self, name):
        print(f"Удален атрибут {name}")
        object.__delattr__(self, name)

d = SafeDict("Killing")
print(d.unknown)
d.key = 10
del d.key

"""
4. Создай класс Employee с приватными полями name и salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError
======================================
5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.dict)  # salary нет
"""

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        self.__salary = value
        if value <= 0:
            raise ValueError("Зарплата дложна быть положительной")
    @salary.deleter
    def salary(self):
        print("Зарплата удалена")
        del self.__salary

e = Employee("Daniil", 5000)
print(e.salary)
e.salary = 8000
print(e.salary)
# e.salary = -100
del e.salary
print(e.__dict__)

"""
6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
"""

class LoginForm:
    def __init__(self):
        self.__username = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        print("[LOG]"
              "Username изменен")
        self.__username = value

form = LoginForm()
form.username = "admin"
print(form.username)

"""
7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **  ** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера.
"""
from datetime import datetime
class Card:
    def __init__(self, number: str):
        self.number = number

    @property
    def number(self):
        return "*" * 12 + self.__number[-4:]
    @number.setter
    def number(self, value):
        if len(value) != 16:
            raise ValueError("Номер должен ссотоять из 16 цифр")
        self.__number = value
    @number.deleter
    def number(self):
        print("[LOG]"
              f"Удален номер в {datetime.now()}")
        del self.__number

test1 = Card("1234456789042345")
assert len(test1.number) == 16, "Неверный номер карты"
assert test1.number == "************2345"
print(test1.number)
test2 = Card("2")
print(test2.number)

"""
8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру.
"""

class UserData:
    def __init__(self, email: str, age: int, is_active: bool):
        self.__email = email
        self.__age = age
        self.__is_active = is_active
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError ("В почте отсутствует - '@'")
        self.__email = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError ("Неверный возраст")
        self.__age = value

    @property
    def is_active(self):
        return self.__is_active
    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError ("Введено неизвестное")
        self.__is_active = value

    @property
    def json(self):
        return {"email": self.email, "age": self.age, "is_active": self.is_active}

test1 = UserData("redlsl.com", 15, True)
assert "@" in test1.email, "Почта без - @"
assert test1.age > 18, "Неверный возраст"
assert test1.json["is_active"] is True