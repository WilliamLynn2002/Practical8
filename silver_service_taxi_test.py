"""Github Link - """

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    my_car = SilverServiceTaxi("Hummer", 100, 2)
    my_car.drive(18)
    print(my_car)
    print(my_car.get_fare())


if __name__ == '__main__':
    main()
