__author__ = 'dimas'

from grab import Grab
from orm import Saver

BASE_URL = 'https://ultimaterewardsearn.chase.com/shopping'


class UltimateRewardsGrabber:

    def __init__(self):
        self.g = Grab()
        self.db_saver = Saver()

    def grab(self):
        self.g.go(BASE_URL)
        divs = self.g.doc.select('//div[contains(@class, "mn_srchListSection")]')
        for div in divs:

            merchants = div.text().split('/$')
            for merchant in merchants:

                try:
                    merchant = merchant.split('Details ')[1]
                    name = ' '.join(merchant.split(' ')[:-2])
                    cost = merchant.split(' ')[-2]
                    print name, ' - ', cost

                    m = self.db_saver.merchants_table.insert()
                    m.execute(name=name, cost=cost)

                except IndexError:
                    pass

    def save(self):
        pass


if __name__ == '__main__':
    #ghost_taleo()
    pass