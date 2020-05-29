"""Github Link - https://github.com/WilliamLynn2002/Practical8/blob/master/taxi_test.py"""

from taxi import Taxi


def main():
    my_car = Taxi("Prius 1", 100)
    my_car.drive(40)
    print(my_car)
    my_car.start_fare()
    my_car.drive(100)
    print(my_car)


if __name__ == '__main__':
    main()
