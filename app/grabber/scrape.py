from grab import Grab
from app import models, db

BASE_URL = 'https://ultimaterewardsearn.chase.com/shopping'


class UltimateRewardsGrabber:

    def __init__(self):
        self.g = Grab()

    def grab(self):
        self.g.go(BASE_URL)
        divs = self.g.doc.select('//div[contains(@class, "mn_srchListSection")]')
        for div in divs:
            try:
                merchants = div.text().split('/$')
                for merchant in merchants:
                    merchant = merchant.split('Details ')[1]
                    title = ' '.join(merchant.split(' ')[:-2])
                    cost = merchant.split(' ')[-2]
                    print title, ' - ', cost
            except IndexError:
                pass
            merchant = models.Item(title=title, cost=cost)
            db.session.add(merchant)
        db.session.commit()


    def save(self):
        pass


if __name__ == '__main__':
    scraper = UltimateRewardsGrabber()
    scraper.grab()