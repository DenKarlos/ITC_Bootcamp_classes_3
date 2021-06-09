class Human:
    default_name = ''
    default_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"House: {self.__house}")
        print(f"Money: {self.__money}")

    @staticmethod
    def default_info():
        print(f'{Human.default_name}')
        print(f'{Human.default_age}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount):
        if self.__money >= house.final_price(discount):
            self.__make_deal(house, house.final_price(discount))
        else:
            print('You have not enoth money to buy this house')


class House:
    def __str__(self):
        return f'area: {self._area} m^2; price: {self._price} $; type: {self.__class__.__name__}.'

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        # print(f"Final price: {final_price}")
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":
    Vasyok = Human('Vasilij', 25)
    Vasyok.info()
    Vasyok.default_info()
    Domik = SmallHouse(10000)
    Vasyok.buy_house(Domik, 0)
    Vasyok.earn_money(11000)
    Vasyok.buy_house(Domik, 10)
    Vasyok.info()
