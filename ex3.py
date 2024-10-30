# Задача 3. Тестирование класса с использованием doctest
# Напишите класс Rectangle, который управляет прямоугольником. Класс должен
# поддерживать следующие методы:
# ● set_dimensions(width, height): устанавливает ширину и высоту
# прямоугольника.
# ● get_area(): возвращает площадь прямоугольника.
# ● get_perimeter(): возвращает периметр прямоугольника.
# Напишите 3 теста с помощью doctest.
# Подсказка № 1
# Убедитесь, что при создании объекта Rectangle с заданными шириной и высотой,
# методы get_area и get_perimeter возвращают правильные значения.
# Подсказка № 2
# После установки новых размеров с помощью set_dimensions, убедитесь, что методы
# get_area и get_perimeter обновляются корректно.
# Подсказка № 3
# Убедитесь, что метод set_dimensions выбрасывает исключение ValueError, если
# переданы отрицательные значения для ширины или высоты.
# Подсказка № 4
# Убедитесь, что метод set_dimensions правильно обрабатывает нулевые значения.
# Для нулевых значений площадь и периметр должны быть корректными (площадь
# будет 0).
from tabnanny import verbose


class Rectangle:
# ● set_dimensions(width, height): устанавливает ширину и высоту
    def __init__(self,width = 0,height  = 0 ):

        """
        Инициализация прямоугольника с заданными шириной и высотой.
        >>> r = Rectangle(3, 4)
        >>> r.get_area()
        12
        >>> r.get_perimeter()
        14
        """

        self.width = width
        self.height = height


    def set_dimensions(self,width, height):
        """
        Устанавливает ширину и высоту прямоугольника.
        >>> r = Rectangle()
        >>> r.set_dimensions(6, 7)
        >>> r.get_area()
        42
        >>> r.get_perimeter()
        26
        """

        if width <0 or height<0:
                raise ValueError("Размер стороны не может быть отрицательным")
        else:
            self.width = width
            self.height = height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return (self.height*2+self.width*2)

import doctest
if __name__ == "__main__":
    doctest.testmod()



