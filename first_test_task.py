# Задание 1
# Написать программу на языке python версии 3, отсеивающую автомобильные
# номера неправильного формата, т.е. проверка ГРЗ типа 1А из проверочного списка.
# Пример списка: ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"].
# Для данного примера правильным ответом будет  ["A123AA11", "А222АА123"].
# Дополнить список верными и неверными номерами. Список для проверки в теле программы (не в файле).
# Приветствуется несколько вариантов решений.

# Подключаем регулярки
import re

# Список номеров
vehicleRegSign_list = ['А123АА11', 'А222АА123',  'р923См16', 'Е100Ее02',
                       '',         'А',          'a12%!df12',
                       'A12AA123', 'A123CC1234', 'AA123A12',
                       'В703АЯ59', 'К404ВЕ112',  'Н217ОР160']
# Первые четыре варианта - верные (регистр не учитывается)
# Не подходят потому что: присутствует недопустимая буква (разрешенные: АВЕКМНОРСТУХ),
# последние два - потому что такого кода региона не существует

# Список уникальных кодов регионов, используемых в знаках
SpecialValidRegionCode_list = [102, 113, 116, 121, 122, 123, 124,
                               125, 126, 134, 136, 138, 142, 147,
                               150, 152, 154, 156, 159, 161, 164,
                               173, 174, 177, 178, 186, 190, 193,
                               196, 197, 198, 199, 702, 716, 750,
                               761, 763, 774, 777, 790, 797, 799]

valid = ""
notValid = ""

# Первый вариант решения
for sign in vehicleRegSign_list:
    # Проверяем правильность текущего знака
    match = re.match(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', sign.upper())
    # Осталось проверить сущесвование данного кода региона:
    regionCode = re.search(r'\d{2,}$', sign)
    if match and regionCode is not None:
        regionCode = regionCode.group()
        # Отбрасываем лишний ноль, имеющийся у регионов со значением < 10, чтобы после конвертировать переменную в число
        if regionCode[0] == '0':
            regionCode = regionCode[1:]
        # Непосредственно проверка на существование:
        if int(regionCode) in SpecialValidRegionCode_list or 1 <= int(regionCode) <= 99:
            valid += sign + ', '
        else:
            notValid += sign + ', '
    # Так и не придумал куда убрать повторяющийся <else>
    else:
        notValid += sign + ', '

# Вывод результатов
print('Valid: ', valid[:-2:], end=';\n')
print('Not valid: ', notValid[:-2:], end=';')


# # Второй вариант решения
# def is_num(possible_num):
#     if re.match(r'\d', possible_num):
#         return True
#     return False
#
#
# def is_right_char(possible_char):
#     if re.match(r'[АВЕКМНОРСТУХ]', possible_char.upper()):
#         return True
#     return False
#
#
# for sign in vehicleRegSign_list:
#     i = 0
#     sign_is_valid = True
#     # Отбрасываем сразу, если маленькая длина строки
#     if len(sign) < 8:
#         sign_is_valid = False
#     else:
#         # Проверям каждый символ строки на корректность
#         for char in sign:
#             i += 1
#             if (2 <= i <= 4 or 7 <= i <= 9) and not is_num(char):
#                 sign_is_valid = False
#                 break
#             elif (i == 1 or 5 <= i <= 6) and not is_right_char(char):
#                 sign_is_valid = False
#                 break
#         # Проверяем код региона
#         regionCode = re.search(r'\d{2,}$', sign).group()
#         if regionCode[0] == '0':
#             regionCode = regionCode[1:]
#         regionCode = int(regionCode)
#         if regionCode not in SpecialValidRegionCode_list and not(1 <= regionCode <= 99):
#             sign_is_valid = False
#     if sign_is_valid:
#         valid += sign + ', '
#     else:
#         notValid += sign + ', '
#
# print('Valid: ', valid[:-2:], end=';\n')
# print('Not valid: ', notValid[:-2:], end=';')
