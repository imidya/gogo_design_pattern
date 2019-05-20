class Character:

    def __init__(self, symbol, size):
        self.symbol = symbol
        self.size = size


class CharacterFactory:

    CACHE = {}

    def get_character(self, symbol, size):
        # TODO
        # CACHE.get(string)
        pass


if __name__ == '__main__':
    factory = CharacterFactory()
    char1 = factory.get_character('Hello', 12)
    char2 = factory.get_character('Happy', 12)
    char3 = factory.get_character('Hello', 12)

    print(char1 == char2)
    print(char1 == char3)
    """Excepted Result
    False
    True
    """
