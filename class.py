# класс это для создания объектов
# класс принимает атрибуты и метод

# практика

#class Product:

    #def __init__(self,name,description,price):
     #   self.name = name
    #    self.description = description
     #   self.price = price

   # def info(self):
    #    print(f)








#class Book:

   # def __init__(self,title,author):
      #  self.title = title
       # self.author = author

   # def describle(self):
      #  print(f"Названия книги {self.title} автор {self.author}")   

# Пример изпользивание
#book1.describle()

#book2 = Book("Мастер и Маргарита","Михаил Булгаков")
#book2.describle()

from statistics import mean

class Student:
    def __init__(self, name: str, grades: list[int | float]):
        self.name = name
        self.grades = grades

    def get_average_grade(self) -> float:
        """Возвращает средний балл студента."""
        if not self.grades:
            return 0.0  # Защита от деления на ноль, если список оценок пуст
        
        return sum(self.grades) / len(self.grades)


# Пример использования:
student1 = Student("Самира", [5, 4, 5, 3, 5])
print(f"Студент: {student1.name}")
print(f"Средний балл: {student1.get_average_grade():.2f}")
