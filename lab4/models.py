

class Engine:

    def __init__(self, power: float, producer: str) -> None:
        self.power = power
        self.producer = producer

    def __repr__(self) -> str:
        return f'''
        Engine power: {self.power}
        Engine producer: {self.producer}'''


class Person:

    def __init__(self, full_name: str) -> None:
        self.full_name = full_name


class Driver(Person):

    def __init__(self, full_name: str, exp: float) -> None:
        Person.__init__(self, full_name)
        self.exp = exp

    def __repr__(self) -> str:
        return f'''
        Driver's name: {self.full_name}
        Driver's experience: {self.exp}'''


class Car(Driver, Engine):

    def __init__(self, model: str, car_class: str, weight: float, driver_name: str, driver_exp: float, eng_power: float, eng_producer: str) -> None:
        self.model = model
        self.car_class = car_class
        self.weight = weight
        Driver.__init__(self, driver_name, driver_exp)
        Engine.__init__(self, eng_power, eng_producer)

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turnRight(self):
        print('Поворот направо')

    def turnLeft(self):
        print('Поворот налево')

    def __repr__(self) -> str:
        return f'''
        Car model: {self.model}
        Car class: {self.car_class}
        Car weight: {self.weight}
        Driver's name: {self.full_name}
        Driver's experience: {self.exp}
        Engine power: {self.power}
        Engine producer: {self.producer}'''


class Lorry(Car):

    def __init__(self, carrying: float, model: str, car_class: str, weight: float, driver_name: str, driver_exp: float, eng_power: float, eng_producer: str) -> None:
        super().__init__(model, car_class, weight, driver_name, driver_exp, eng_power, eng_producer)
        self.carrying = carrying

    def __repr__(self) -> str:
        return f'''
        Car carrying: {self.carrying}
        {super().__repr__()}
        '''

class SportCar(Car):

    def __init__(self, speed: float, model: str, car_class: str, weight: float, driver_name: str, driver_exp: float, eng_power: float, eng_producer: str) -> None:
        super().__init__(model, car_class, weight, driver_name, driver_exp, eng_power, eng_producer)
        self.speed = speed

    def __repr__(self) -> str:
        return f'''
        Car speed: {self.speed}
        {super().__repr__()}
        '''