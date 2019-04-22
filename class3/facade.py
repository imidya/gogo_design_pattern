class SubSystem1:
    def hahaha(self):
        print('子系統一方法')


class SubSystem2:
    def yoyoyo(self):
        print('子系統二方法')


class Facade:
    # TODO
    pass


if __name__ == '__main__':
    facade = Facade()

    facade.methodA()
    """Excepted Result
    子系統二方法
    """
    facade.methodB()
    """Excepted Result
    子系統一方法
    """
    facade.methodC()
    """Excepted Result
    子系統二方法
    子系統一方法
    """
