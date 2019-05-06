from queue import Queue


class Memento:
    def __init__(self, state):
        self.state = state


class Application:
    state = 'init state'

    def backup(self) -> Memento:
        return Memento(self.state)

    def rollback(self, memento: Memento):
        self.state = memento.state

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return self.state


class RecoverManager:
    q = Queue()

    def add(self, memento: Memento):
        self.q.put(memento)

    def get(self) -> Memento:
        return self.q.get()


if __name__ == '__main__':
    recover = RecoverManager()
    app = Application()
    print(app)

    app.set_state('State 2')
    m = app.backup()
    recover.add(m)
    print(app)

    app.set_state('State 3')
    m = app.backup()
    recover.add(m)
    print(app)

    new_m = recover.get()
    app.rollback(new_m)
    print(app)

    """Excepted Result
    init state
    State 2
    State 3
    State 2
    """
