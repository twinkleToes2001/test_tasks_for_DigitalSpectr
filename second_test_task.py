# Задание 2
# Реализовать алгоритм поиска случайной точки на декартовой системе координат относительно заданной точки.
# Поиск должен быть максимально быстрым. Выводить промежуточные результаты.
# Входные данные (вводятся пользователем): w, h, - ширина и высота сетки; (x0, y0) - стартовая точка.
# Координаты искомой точки заранее неизвестны. Для создания искомой точки использовать класс SearchPoint.
# Для сравнения точки на каждом шагу с искомой пользоваться функцией where_is_point, которая возвращает строку,
# описывающую положение искомой точки относительно текущей: выше("U"), правее и выше("RU"), левее("L"), ниже("D") и т.п;
# если функция возвращает пустую строку, то точка текущая точка совпадает с искомой.
# Пример:
# 	входные данные:
# 	w h 10 10
# 	x0 y0 2 9
# 	Выходные данные (x, y):
# 	6 4
# 	4 2
# 	5 2
# 	Искомая точка: (5, 2)

from random import randint


# Класс искомой точки
class SearchPoint:
    def __init__(self, w, h):
        # Инициализация случайных координат искомой точки
        self.__x = randint(0, w - 1)
        self.__y = randint(0, h - 1)

    def where_is_point(self, x, y):
        # Описывает положение искомой точки относительно текущей.
        # Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
        pos_x = pos_y = ' '
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'U'
        elif y < self.__y:
            pos_y = 'D'
        return pos_x + pos_y

    # Создание <системы координат> на котором отмечены:
    # <I>(Initial) - начальная точка, <T>(Target) - искомая точка, <·> - ничем не занятое пространство
    def create_field(self, w, h, x_initial, y_initial):
        # Проверяем если координаты искомой и начальной точки совпали:
        if x_initial == self.__x and y_initial == self.__y:
            print('Везунчик! Вероятность такого исхода ' + str((1 / (w * h)) ** 2) + '! (вроде бы ¯\_(ツ)_/¯)')
        else:
            print()
            # Создание массива
            field = []
            for j in range(0, h):
                # Добавление в массив элементов
                field.append([])
                for i in range(0, w):
                    field[j].append('')
                    if i == self.__x and j == self.__y:
                        field[j][i] = 'T'
                    elif i == x_initial and j == y_initial:
                        field[j][i] = 'I'
                    else:
                        field[j][i] = '·'
                    # Сразу же делаем вывод + несколько отступов
                    print(field[j][i], end='')
                print()
            print()

    # Геттеры класса
    def get_x(self):
        return str(self.__x)

    def get_y(self):
        return str(self.__y)


# Ввод ширины и высоты поля
width = int(input('Width?: '))
height = int(input('Height?: '))
# Создание искомой точки
SP = SearchPoint(width, height)
# Вывод ее координат
print('Координаты искомой точки: ' + SP.get_x() + ' ' + SP.get_y(), end=';\n')
# Вввод данных для начальной точки
x0 = int(input('x0? (значения 0 <= x0 <= ' + str(width - 1) + '): '))
y0 = int(input('y0? (значения 0 <= y0 <= ' + str(height - 1) + '): '))
print('Координаты начальной точки: ' + str(x0) + ' ' + str(y0), end=';\n')
# Темповые ширина и высота, используемые далее для выполнения задания,
# чтобы не терять нужные первоначальные значения ширины и высоты
temp_width = width
temp_height = height
# Создаем поле
SP.create_field(width, height, x0, y0)
# Определяем позицию точки (обязательно до цикла), и закидываем это значение в переменную
position = SP.where_is_point(x0, y0)


# Бегаем пока функция where_is_point не вернет два пробела, что будет означать что точка найдена
while position[0] != ' ' or position[1] != ' ':
    # Делаем проверку, чтобы темповые переменные не стали нулем, иначе получим бесконечный цикл
    if temp_width // 2 != 0:
        temp_width //= 2
    # Для X:
    # Мониторим возможный out_of_bounds для X и Y с помощью if-else, так же определяем новые координаты
    if position[0] == 'L':
        if x0 - temp_width < 0:
            x0 = 0
        else:
            x0 = x0 - temp_width
    elif position[0] == 'R':
        if x0 + temp_width > width - 1:
            x0 = width - 1
        else:
            x0 = x0 + temp_width
    # Для Y:
    if temp_height // 2 != 0:
        temp_height //= 2
    if position[1] == 'U':
        if y0 - temp_height < 0:
            y0 = 0
        else:
            y0 = y0 - temp_height
    elif position[1] == 'D':
        if y0 + temp_height > height - 1:
            y0 = height - 1
        else:
            y0 = y0 + temp_height
    # Вывод промежуточных результатов:
    print(str(x0) + ' ' + str(y0), end=';\n')
    # В конце итерации определяем местоположение точки, чтобы цикл не отрабатывал лишнюю итерацию
    # (как если бы мы поставили эту операцию в начале цикла)
    position = SP.where_is_point(x0, y0)


# # То же самое только создается пять тестов с произвольной генераций значений
# for i in range(5):
#     # Рандомная генерация ширины и высоты поля
#     width = randint(1, 30)
#     height = randint(1, 30)
#     SP = SearchPoint(width, height)
#     print('Координаты искомой точки: ' + SP.get_x() + ' ' + SP.get_y(), end=';\n')
#     # Рандомная генерация координат начальной точки
#     x0 = randint(0, width - 1)
#     y0 = randint(0, height - 1)
#     print('Координаты начальной точки: ' + str(x0) + ' ' + str(y0), end=';\n')
#     temp_width = width
#     temp_height = height
#     SP.create_field(width, height, x0, y0)
#     position = SP.where_is_point(x0, y0)
#
#     while position[0] != ' ' or position[1] != ' ':
#         if temp_width // 2 != 0:
#             temp_width //= 2
#         if position[0] == 'L':
#             if x0 - temp_width < 0:
#                 x0 = 0
#             else:
#                 x0 = x0 - temp_width
#         elif position[0] == 'R':
#             if x0 + temp_width > width - 1:
#                 x0 = width - 1
#             else:
#                 x0 = x0 + temp_width
#         if temp_height // 2 != 0:
#             temp_height //= 2
#         if position[1] == 'U':
#             if y0 - temp_height < 0:
#                 y0 = 0
#             else:
#                 y0 = y0 - temp_height
#         elif position[1] == 'D':
#             if y0 + temp_height > height - 1:
#                 y0 = height - 1
#             else:
#                 y0 = y0 + temp_height
#         print(str(x0) + ' ' + str(y0), end=';\n')
#         position = SP.where_is_point(x0, y0)


