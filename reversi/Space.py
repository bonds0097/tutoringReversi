class Space(object):
    """docstring for Space"""
    def __init__(self, x, y):
        super(Space, self).__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        return self.__repr__()


