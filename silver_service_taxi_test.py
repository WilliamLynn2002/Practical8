"""Github Link - https://github.com/WilliamLynn2002/Practical8/blob/master/silver_service_taxi_test.py"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    my_car = SilverServiceTaxi("Hummer", 100, 2)
    my_car.drive(18)
    print(my_car)
    print(my_car.get_fare())


if __name__ == '__main__':
    main()
