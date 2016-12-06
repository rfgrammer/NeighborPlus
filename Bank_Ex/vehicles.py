from abc import ABCMeta, abstractmethod


class Vehicle(object):

    __metaclass__ = ABCMeta

    base_sale_price = 0.0
    wheels = 0

    def __init__(self, miles, wheels, maker, model, year, sold_on):
        self.wheels = wheels
        self.maker = maker
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.miles = miles

    def sale_price(self):
        if self.sold_on is not None:
                return 0.0
        return 5000 * self.wheels

    def purchase_price(self):
        if self.sold_on is not None:
                return 0.0
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        pass


class Car(Vehicle):

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'


class Truck(Vehicle):

    base_sale_price = 10000
    wheels = 0

    def vehicle_type(self):
        return 'truck'


class KoreanCar(Car):

    def newfunc(self):
        return 'New function'


def main():
    mycar = Car(1000, 4, 'Ford', 'Mustang', 1996, None)
    print(mycar.purchase_price())

    mytruck = Truck(2000, 6, 'GMC', 'F150', 2000, None)
    print(mytruck.purchase_price())

    myabs = Vehicle(2000, 6, 'GMC', 'F150', 2000, None)
    myabs.base_sale_price = 7000
    print(myabs.purchase_price())

    korcar = KoreanCar(1000, 4, 'Ford', 'Mustang', 1996, None)
    print(korcar.newfunc())

if __name__ == '__main__':
    main()
