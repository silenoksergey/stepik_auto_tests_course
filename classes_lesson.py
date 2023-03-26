class Car():
    """Создание общий класс машины"""
    def __init__(self, model, year, engine_displacement, price, mileage):
        """Инициализируем атрибуты машины"""
        self.model = model
        self.year = year
        self.engine_displacement = engine_displacement
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4
    def description_car(self):
        """Получения описания машины"""
        description = "Модель - " + self.model + ", год выпуска - " + str(self.year) + ", объём двигателя - " +\
        str(self.engine_displacement) + ", цена - " + str(self.price) + "р." + ", пробег - " + str(self.mileage) + "км" + ", колёс - " + str(self.number_of_wheels)
        print("Описание машины:", description)
class truck(Car):
    """Создаём класс наследник - Грузовик"""
    def __init__(self, model, year, engine_displacement, price, mileage):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(model, year, engine_displacement, price, mileage)
        self.number_of_wheels = 8
car = Car("XC90", 2021, 2.0, 7500000, 29125)
car.description_car()
truck = truck("HOWO", 2020, 14.8, 9300000, 20000)
truck.description_car()