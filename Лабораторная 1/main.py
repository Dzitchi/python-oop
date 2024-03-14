from typing import Union
import doctest


class Mouse:
    def __init__(self, charge: Union[int], sensitivity: Union[int]):
        """
        Создание и подготовка к работе объекта "Компьютерная мышь"

        :param charge: Заряд мыши
        :param sensitivity: Чувствительность

        Примеры:
        >>> mouse = Mouse(100, 400)
        """
        if not isinstance(charge, int):
            raise TypeError(charge, "type error, weight must be int")
        if charge < 0 or charge > 100:
            raise ValueError(charge, "charge must be between 0 and 100")
        self.weight = charge

        if not isinstance(sensitivity, int):
            raise TypeError(sensitivity, "type error, weight must be int")
        if sensitivity <= 0:
            raise ValueError(sensitivity, "is less than zero")
        self.sensitivity = sensitivity

    def is_charged(self) -> bool:
        """
        Функция которая проверяет не разряжена ли мышь

        :return: Является ли мышь заряженной

        Примеры:
        >>> mouse = Mouse(0, 400)
        >>> mouse.is_charged()
        """
        ...

    def change_sensitivity(self, sensitivity: Union[int]) -> None:
        """
        Изменение чувствительности мыши
        :param sensitivity: то какую чувствительность нужно установить

        Примеры:
        >>> mouse = Mouse(100, 400)
        >>> mouse.change_sensitivity(200)
        """
        if not isinstance(sensitivity, int):
            raise TypeError(sensitivity, "sensitivity must be int")
        if sensitivity <= 0:
            raise ValueError(sensitivity, "sensitivity must be greater than zero")
        ...


class Kettle:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float], temperature: Union[int]):
        """
        Создание и подготовка к работе объекта "Чайник"

        :param capacity_volume: Объем чайника
        :param occupied_volume: Заполненный объем
        :param temperature: Температура воды

        Примеры:
        >>> kettle = Kettle(700, 400, 22)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError(capacity_volume, "capacity volume must be int or float")
        if capacity_volume <= 0:
            raise ValueError(capacity_volume, "capacity volume must be greater than zero")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError(occupied_volume, "occupied volume must be int or float")
        if occupied_volume <= 0 or occupied_volume > capacity_volume:
            raise ValueError(occupied_volume, "occupied volume must be greater than zero and less than capacity volume")
        self.occupied_volume = occupied_volume

        if not isinstance(temperature, int):
            raise TypeError(temperature, "temperature must be int")
        if temperature > 100 or temperature < 0:
            raise ValueError(temperature, "temperature must be between 0 and 100")
        self.temperature = temperature

    def is_boiled(self) -> bool:
        """
        Функция которая проверяет что вода 100 градусов

        :return: Является ли вода кипятком

        Примеры:
        >>> kettle = Kettle(700, 500, 100)
        >>> kettle.is_boiled()
        """
        ...

    def add_water(self, water: Union[int, float]) -> None:
        """
        Добавление воды в чайник.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если добавляем воды больше, чем может поместится в чайник то вызываем ошибку

        Примеры:
        >>> kettle = Kettle(700, 200, 22)
        >>> kettle.add_water(400)
        """
        if not isinstance(water, (int, float)):
            raise TypeError(water, "must be int or float")
        if water < 0:
            raise ValueError(water, "must be greater than zero")
        ...

    def remove_water(self, water: Union[int, float]) -> None:
        """
        Извлечение воды из чайника.
        :param water: Объем извлекаемой жидкости

        :raise ValueError: Если извлекаем воды больше, чем есть в чайникк то вызываем ошибку

        Примеры:
        >>> kettle = Kettle(700, 500, 22)
        >>> kettle.remove_water(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError(water, "must be int or float")
        if water < 0:
            raise ValueError(water, "must be greater than zero")
        ...


class Auto:
    def __init__(self, speed: Union[int], gas: Union[int]):
        """
        Создфние и подготовка к работе объекта "автомобиль"

        :param speed: скорость автомобиля
        :param gas: количество топлива

        Примеры:
        >>> auto = Auto(0, 20)
        """
        if not isinstance(speed, int):
            raise TypeError(speed, "speed must be int")
        self.speed = speed
        if not isinstance(gas, int):
            raise TypeError(gas, "gas must be int")
        if gas < 0:
            raise ValueError(gas, "gas must be greater than zero")

    def is_gas_empty(self) -> bool:
        """
        Функция проверяет, что топливный бак пуст

        :return: пуст ли топливный бак

        Примеры:
        >>> auto = Auto(0, 0)
        >>> auto.is_gas_empty()
        """
        ...

    def accelerate(self, speed: Union[int]) -> None:
        """
        Добавление скорости автомобилю
        :param speed: На сколько увеличить скорость

        :raise ValueError: Если количество топлива равно нулю вызвать исключение

        Примеры:
        >>> auto = Auto(0, 20)
        >>> auto.accelerate(40)
        """
        if not isinstance(speed, int):
            raise TypeError(speed, "speed must be int")
        if speed < 0:
            raise ValueError(speed, "speed must be greater than zero")
        ...

    def braking(self, speed: Union[int]) -> None:
        """
        Уменьшение скорости автомобилю
        :param speed: На сколько уменьшить скорость

        :raise ValueError: Если скорость равно нулю вызвать исключение

        Примеры:
        >>> auto = Auto(60, 20)
        >>> auto.braking(40)
        """
        if not isinstance(speed, int):
            raise TypeError(speed, "speed must be int")
        if speed < 0:
            raise ValueError(speed, "speed must be greater than zero")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
