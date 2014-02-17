__author__ = 'dimas'


class Merchant(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return "<Merchant('%s','%s'')>" % (self.name, self.cost)
