"""
Template Method Pattern

只有兩種套餐的簡餐店
點餐 -> 收錢 -> 找零 -> 準備主餐 -> 準備附湯 -> 送餐
"""


class Meal:
    price = None
    name = None

    def start_order(self):
        print(f'客人點餐：{self.name}')

    def charge(self):
        print('收錢')

    def return_money(self, money_from_customer):
        return_money = money_from_customer - self.price
        print(f'找零：{return_money}')

    def prepare_main_meal(self):
        pass

    def prepare_soup(self):
        pass

    def deliver(self):
        print('送餐給客人')

    def process_order(self, money_from_customer):
        # TODO
        pass


class BeefNoodleMeal:
    price = 110
    name = '牛肉乾麵'
    # TODO


class BraisedPorkMeal:
    price = 75
    name = '滷肉飯'
    # TODO


if __name__ == '__main__':
    beef_noodle = BeefNoodleMeal()
    braised_pork = BraisedPorkMeal()

    beef_noodle.process_order(150)
    """Excepted Results
    客人點餐：牛肉乾麵
    收錢
    找零：40元
    準備主餐 - 煮麵
    準備主餐 - 加牛肉
    準備附湯 - 牛肉湯
    送餐給客人
    """

    braised_pork.process_order(100)
    '''Excepted Results
    客人點餐：滷肉飯
    收錢
    找零：25元
    準備主餐 - 裝飯
    準備主餐 - 淋滷肉
    準備附湯 - 餛飩湯
    送餐給客人
    '''
