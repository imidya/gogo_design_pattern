import abc


class Meal(abc.ABC):
    @abc.abstractmethod
    def get_content(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def price(self):
        raise NotImplementedError()


class BigMac(Meal):

    def get_content(self):
        return '大麥克'

    def price(self):
        return 109


class FiletOFish(Meal):

    def get_content(self):
        return '麥香魚'

    def price(self):
        return 89


class SideDishA(Meal):

    def __init__(self, meal):
        self.meal = meal

    def get_content(self):
        return self.meal.get_content() + ' | 薯條 | 可樂'

    def price(self):
        return self.meal.price() + 30


if __name__ == '__main__':
    big_mac = BigMac()
    filet_o_fish = FiletOFish()

    big_mac_sidedish_a = SideDishA(big_mac)
    filet_o_fish_sidedish_a = SideDishA(filet_o_fish)

    print(big_mac_sidedish_a.get_content())
    print(big_mac_sidedish_a.price())
    print(filet_o_fish_sidedish_a.get_content())
    print(filet_o_fish_sidedish_a.price())
    """Excepted Result
    大麥克 | 薯條 | 可樂
    139
    麥香魚 | 薯條 | 可樂
    119
    """
