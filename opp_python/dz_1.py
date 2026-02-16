"""
++++++++++++++++++++++++++++++++++
Классы и атрибуты
++++++++++++++++++++++++++++++++++
Задание 1, 2:

1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
Проверь, как это повлияло на значения у обоих объектов.
Убедись, что dict объектов отражает изменения.

2. Добавь в класс Dog строку документации, описывающую его назначение.
Затем выведи её на экран.
После этого добавь в объект класса новые атрибуты name и age,
а затем удали name.
Проверь, что произойдёт при попытке снова вывести объект.name.
Решение:
"""

class Dog:
    "Класс отражающий породу и количество конечностей собаки"
    species = "canis"
    legs = 4
a = Dog()
b = Dog()
a.species = "sobaka"
print(a.species)
print(a.__dict__)
print(Dog.__dict__)
print(Dog.__doc__)
b.name = "Tali"
setattr(a, "age", 3)
delattr(b, "name")
print(b.name)
print("Получается ошибка, так как этого атрибута нет ни в классе, ни в объекте.")

"""
Задача 3: 
Создай класс User с атрибутами класса role = "guest" и active = True.
С помощью функций getattr(), setattr(), hasattr() и delattr():

измени значение role на "admin",
проверь наличие active,
добавь новый атрибут email,
удали role.
Убедись, что всё работает корректно, и выведи итоговое содержимое dict класса User.
Решение:
"""

class User:
    role = "guest"
    active = True
setattr(User, "role", "admin")
print(getattr(User, "active"))
setattr(User, "email", "text@icloud.com")
print(hasattr(User, "email"))
delattr(User, "role")
print(User.__dict__)