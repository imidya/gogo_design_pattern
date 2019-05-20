import abc


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError()


class Subject(abc.ABC):

    _observers = []

    def attach(self, observer):
        # TODO
        pass

    def notify(self):
        # TODO
        pass

    def detach(self, observer):
        for i, o in enumerate(self._observers):
            if o == observer:
                self._observers.remove(o)
                break


class PieChart(Observer):

    def __init__(self, m):
        self.model = m

    def update(self):
        print(f'Update PieChart: {self.model.get_value()}')


class BarChart(Observer):

    def __init__(self, m):
        self.model = m

    def update(self):
        print(f'Update BarChart: {self.model.get_value()}')


class Model(Subject):

    value = 0

    def set_value(self, value):
        # TODO: when value updated, notify observers to update value
        pass

    def get_value(self):
        return self.value


if __name__ == '__main__':
    model = Model()
    pie_chart = PieChart(model)
    bar_chart = BarChart(model)
    # TODO: attach observers(pie_chart and bar_chart) to subject(model)

    model.notify()
    """Excepted Result
    Update PieChart: 0
    Update BarChart: 0
    """
    print()

    model.set_value(999)
    """Excepted Result
    Update PieChart: 999
    Update BarChart: 999
    """
    print()

    model.detach(pie_chart)
    model.set_value(9487)
    """Excepted Result
    Update BarChart: 9487
    """
