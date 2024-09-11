class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            self.__is_valid_vin(vin)
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) is False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        symbol_number = ['A', 'B', 'C', 'E', 'K', 'M', 'O', 'P', 'T', 'Y', 'H', 'X']
        num_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if isinstance(numbers, str) is False:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        if (numbers[0] not in symbol_number or
            numbers[1] not in num_number or
            numbers[2] not in num_number or
            numbers[3] not in num_number or
            numbers[4] not in symbol_number or
            numbers[5] not in symbol_number):
            raise IncorrectCarNumbers('Некорректный номер')
        else:
            return True

try:
  first = Car('Model1', 1000000, 'X777XX')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')