__author__ = 'dimas'

from grab import Grab

BASE_URL = 'https://ultimaterewardsearn.chase.com/shopping'

class UltimateRewardsGrabber:

    def __init__(self):
        self.g = Grab()

    def grab(self):
        self.g.go(BASE_URL)
        divs = self.g.doc.select('//div[contains(@class, "mn_srchListSection")]')

    def save(self):
        pass


if __name__ == '__main__':
    #ghost_taleo()
    pass