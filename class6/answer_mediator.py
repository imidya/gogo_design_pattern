import abc


class UN:

    def talk_to_us(self, country, msg):
        print(f'{country.name} talk to US, says {msg}')


class Country(abc.ABC):

    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name


class US(Country):
    pass


class UK(Country):
    def talk_to_US(self, msg):
        self.mediator.talk_to_us(self, msg)


if __name__ == '__main__':
    UN = UN()
    US = US(UN, 'US')
    UK = UK(UN, 'UK')

    UK.talk_to_US('Trade War')
