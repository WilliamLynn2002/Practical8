"""Github Link - https://github.com/WilliamLynn2002/Practical8/blob/master/unreliable_car_test.py"""

from unreliable_car import UnreliableCar


def main():
    """Test some unreliable cars"""

    # create cars with different reliabilities
    car_one = UnreliableCar("Car 1", 100, 90)
    car_two = UnreliableCar("Car 2", 100, 10)

    # attempt to drive the cars 10 times
    # output what distance they drove
    for i in range(1, 11):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(car_one.name, car_one.drive(i)))
        print("{:12} drove {:2}km".format(car_two.name, car_two.drive(i)))

    # print the final states of the cars
    print(car_one)
    print(car_two)


if __name__ == '__main__':
    main()
