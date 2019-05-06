from typing import List, Text


class SearchAlgorithm:

    def do_search(self) -> List[Text]:
        pass


# TODO: SearchAlgorithmA


# TODO: SearchAlgorithmB


class User:
    def __init__(self, uid):
        self.uid = uid


class SearchEngine:
    def search(self, user: User):
        strategy = None

        if user.uid % 2 == 0:
            # TODO
            pass
        else:
            # TODO
            pass

        items: List[Text] = strategy.do_search()
        print(items)


if __name__ == '__main__':
    search_engine = SearchEngine()
    user_A = User(2)
    user_B = User(3)

    search_engine.search(user_A)
    """Excepted Result
    ['Item A', 'Item B', 'Item C']
    """
    print()

    search_engine.search(user_B)
    """Excepted Result
    ['Item C', 'Item B', 'Item A']
    """