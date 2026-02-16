"""
======================================
1. Создай класс LengthValidator, который:
принимает в init минимальную и максимальную длину строки;
в call проверяет, что длина переданной строки в заданном диапазоне;
выбрасывает ValueError, если условие не выполнено.
Пример:
validator = LengthValidator(3, 10)
print(validator("python"))  # True
print(validator("hi"))      # ValueError
======================================
"""
class LengthValidator:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def __call__(self, dip):
        if self.min <= len(dip) <= self.max:
            return True
        else:
            raise ValueError

validator = LengthValidator(3, 10)
print(validator("python"))
print(validator("hi"))

"""
======================================
2. Создай класс Sumator, который:
при первом вызове принимает число;
каждый следующий вызов увеличивает сумму;
хранит и возвращает текущую сумму.
Пример:
s = Sumator()
print(s(5))   # 5
print(s(10))  # 15
print(s(-2))  # 13
======================================
"""
class Sumator:
    def __init__(self):
        self.count = 0
    def __call__(self, name):
        self.count += name
        return self.count
s = Sumator()
print(s(5))
print(s(10))
print(s(-2))

"""
======================================
3. Создай класс HasText, который:
в init принимает ожидаемую подстроку;
в call принимает текст и возвращает True, если подстрока найдена.
Подумай как сделать так, чтобы работало как и в примере?
Пример:
assert HasText("Success")("Test passed: Success")  # True
assert HasText("Error")("All OK")  # False
======================================
"""
class HasText:
    def __init__(self, stroka):
        self.text = stroka
    def __call__(self, text):
        if self.text in text:
            return True
        else:
            return False
res = HasText("Success")("Test passed: Success")
res = HasText("Error")("All OK")
assert HasText("Success")("Test passed: Success")
assert HasText("Error")("All OK")

"""
======================================
4. Создай класс Book, который хранит:
название книги (title)
автора (author)
Переопредели str и repr, чтобы:
print(book) выводил "Автор — Название"
repr(book) показывал <Book 'Название' by Автор>
Пример:
book = Book("1984", "Джордж Оруэлл")
print(book)         # Джордж Оруэлл — 1984
print(repr(book))   # <Book '1984' by Джордж Оруэлл>
======================================
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.author} - {self.title}"
    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
book = Book("1984", "Джордж Оруэлл")
print(book)
print(repr(book))

"""
======================================
5. Создай класс TestUser, который содержит id, name, email.
Переопредели repr, чтобы его было удобно видеть в логах автотеста:
user = TestUser(12, "Daniil", "daniil@example.com")
print(user)
# <TestUser id=12 name='Daniil' email='daniil@example.com'>
"""
class TestUser:
    def __init__(self, us_id, name, email):
        self.us_id = us_id
        self.name = name
        self.email = email
    def __repr__(self):
        return f"<TestUser id={self.us_id} name={self.name} email={self.email}>"
user = TestUser(12, "Daniil", "daniil@example.com")
print(user)