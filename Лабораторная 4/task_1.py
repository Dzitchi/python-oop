class Vehicle:
    """Базовый класс для всех видов транспортных средств."""

    def __init__(self, brand: str, engine: bool = False):
        """
        Конструктор базового класса.

        :param brand: Марка транспортного средства.
        :param engine: Запущен ли двигатель транспортного средства.
        """
        self.brand = brand
        self.engine = engine

    def switch_eng(self) -> None:
        """
        Метод, запускающий или выключающий двигатель.
        """
        ...

    def honk(self) -> None:
        """
        Метод, который включает гудок транспортного средства.
        """
        ...

    def __str__(self) -> str:
        return f"Марка: {self.brand}, Двигатель запущен: {self.engine}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}', {self.engine})"


class Car(Vehicle):
    """Дочерний класс, представляющий легковое автомобиль."""

    def __init__(self, brand: str, num_doors: int, engine: bool = False):
        """
        Конструктор дочернего класса.

        :param brand: Марка автомобиля.
        :param engine: Запущен ли двигатель транспортного средства.
        :param num_doors: Количество дверей у автомобиля.
        """
        super().__init__(brand, engine)
        self.num_doors = num_doors

    def honk(self) -> None:
        """
        Метод, который включает гудок транспортного средства.
        Перегрузка метода нужна, так как звук автомобиля отличается от базового
        """
        ...

    def __str__(self) -> str:
        return f"{super().__str__()}, Количество дверей {self.num_doors}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}', {self.num_doors}, {self.engine})"
