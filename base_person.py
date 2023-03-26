class Person():
    """"Созадём человека"""

    def __init__(self, name, age, height):
        """"Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100
    def description_person(self):
        """"Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)
        print("Нового человека зовут: ", description)

    def get_weight(self):
        """"Получение веса человека"""
        print("Вес нашего человека: "+ str(self.weight))

    def update_weight(self, kg):
        """"Изменение веса человека"""
        self.weight = kg

class Warrior(Person):
    """Создаём класс воина"""
    def __init__(self, name, age, height):
        """"Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100
    def get_rage(self):
        """"Заряд ярости воина"""
        print("Заряд ярости равен: "+ str(self.rage))

    def description_person(self):
        """"Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)
        # print("Нового человека зовут: ", description)
        return description

