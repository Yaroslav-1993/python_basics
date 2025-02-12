"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, m_values):
        self.m_values = m_values

    def __str__(self):
        result = '\n'.join(['  '.join([item for item in row]) for row in self.m_values])
        return result

    def __add__(self, other):

        pass # Сравнение размерности
        result = [[self.m_values[i][j] + other.m_values[i][j] for j in range(len(self.m_values[0]))] for i in range(len(self.m_values))]
        return result


matrix_1 = Matrix([['a','b'], ['c', 'd'], ['e', 'f']])
matrix_2 = Matrix([['a','b'], ['c', 'd'], ['e', 'f']])
print(f'Матрица 1:\n{matrix_1}')
print(f'Матрица 2:\n{matrix_1}')
new_matrix = matrix_1 + matrix_2
nl = '\n'
print(f'Сумма матриц:\n{nl.join(["  ".join([item for item in row]) for row in new_matrix])}')
