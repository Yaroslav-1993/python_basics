"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    # Публичные атрибуты
    thickness = 0.05
    density = 25

    # Защищённые атрибуты экземпляра класса
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self):
        result = self.thickness*self.density*self._length*self._width
        return result


r_1 = Road(1000, 50)
print(r_1.asphalt_weight())

