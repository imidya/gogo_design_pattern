import abc


class Drawer(abc.ABC):

    @abc.abstractmethod
    def forward(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def rotate(self):
        raise NotImplementedError()


class TwoDDrawer(Drawer):
    # TODO


class ThreeDDrawer(Drawer):
    # TODO


class Maze:

    def __init__(self, drawer):
        self.drawer = drawer
    
    def forward(self):
        self.drawer.forward()

    def rotate(self):
        self.drawer.rotate()

    def set_drawer(self, drawer):
        self.drawer = drawer


if __name__ == '__main__':
    maze = Maze(TwoDDrawer())
    maze.forward()
    maze.rotate()

    maze.set_drawer(ThreeDDrawer())
    maze.forward()
    maze.rotate()

    """Excepted Result
    2D forward
    2D rotate
    3D forward
    3D rotate
    """
