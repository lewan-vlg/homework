class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class IncorrectNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)


    def __is_valid_vin(self, __vin):
        if not isinstance(__vin, int):
            raise IncorrectVinNumber('Некорректный тип VIN номер')

        if  __vin < 1000000 or __vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectNumbers('Некорректный тип данных для номеров')

        if  len(__numbers) != 6:
            raise IncorrectNumbers('Неверная длина номера')

        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')