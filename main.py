'''
Погружение в Python (семинары)
Урок 15. Обзор стандартной библиотеки Python
1. Решить задания, которые не успели решить на семинаре.
2. Возьмите любые 1-3 задания из прошлых домашних заданий. 
    - Добавьте к ним логирование ошибок и полезной информации. 
    - Также реализуйте возможность запуска из командной строки с передачей параметров.
    Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" 
    "Зачет" ставится, если Слушатель успешно выполнил задание. 
    "Незачет" ставится, если Слушатель не выполнил задание. 
    Критерии оценивания: 
    1 - Слушатель написал корректный код для задачи, добавил к ним логирование ошибок и полезной информации.
'''
import doctest
import logging
import argparse
import sys

# Настройка логирования в файл с кодировкой UTF-8
handler = logging.FileHandler('rectangle_log.txt', mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Создание логгера
logger = logging.getLogger()
logger.setLevel(0)
logger.addHandler(handler)

class NegativeValueError(Exception):
    def __init__(self, message="Отрицательные значения не допускаются"):
        self.message = message
        super().__init__(self.message)
        
class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
        logging.info(f"Создан {self}")
  
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            logging.error(f"Ширина должна быть положительной, а не {value}")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            logging.error(f"Высота должна быть положительной, а не {value}")
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        self._height = value

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        perimeter = 2 * (self.width + self.height)
        logging.info(f"Периметр {self}: {perimeter}")
        return perimeter

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        area = self.width * self.height
        logging.info(f"Площадь {self}: {area}")
        return area

    def __add__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        '''
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        logging.info(f"Сложение {self} и {other}: {width}, {height}")
        return Rectangle(width, height)

    def __sub__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        '''
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        logging.info(f"Вычитание {other} из {self}: {width}, {height}")
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        result = self.area() < other.area()
        logger.info(f"{self} < {other}: {result}")
        return result

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        result = self.area() == other.area()
        logger.info(f"{self} == {other}: {result}")
        return result

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        result = self.area() <= other.area()
        logger.info(f"{self} <= {other}: {result}")
        return result

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"
    
def main(width1, height1, width2, height2):
    logger.info(f"Получены параметры: width1={width1}, height1={height1}, width2={width2}, height2={height2}")
    rect1 = Rectangle(width1, height1)
    rect2 = Rectangle(width2, height2)

    print(f"Периметр rect1: {rect1.perimeter()}")  
    print(f"Площадь rect2: {rect2.area()}")    
    print(f"rect1 < rect2: {rect1 < rect2}")        
    print(f"rect1 == rect2: {rect1 == rect2}")   
    print(f"rect1 <= rect2: {rect1 <= rect2}")     

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}") 
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Работа с прямоугольниками.')
    parser.add_argument('width1', type=float, help='Ширина первого прямоугольника')
    parser.add_argument('height1', type=float, help='Высота первого прямоугольника')
    parser.add_argument('width2', type=float, help='Ширина второго прямоугольника')
    parser.add_argument('height2', type=float, help='Высота второго прямоугольника')

    args = parser.parse_args()

    main(args.width1, args.height1, args.width2, args.height2)