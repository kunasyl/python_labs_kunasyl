from models import SportCar, Car

def init():
    car = Car(
        # speed = 200,
        model = 'Toyota', 
        car_class = 'Camry', 
        weight = 5, 
        driver_name = 'John Doe',
        driver_exp = 7,
        eng_power = 8.0,
        eng_producer = 'Japan',
        )
    print(car)
    car.start()
    car.turnLeft()
    car.turnRight()
    car.stop()

if __name__ == '__main__':
    init()