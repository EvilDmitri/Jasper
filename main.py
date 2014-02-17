__author__ = 'dimas'

from grabber.scrape import UltimateRewardsGrabber


def main():
    scraper = UltimateRewardsGrabber()
    scraper.grab()

if __name__ == '__main__':
    main()