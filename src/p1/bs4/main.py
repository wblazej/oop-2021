from typing import List
import requests
from bs4 import BeautifulSoup


class Offer:
    name: str
    title: str
    price: str
    posted_at: str

    def __init__(self, name):
        self.name = name

    def scrap(self):
        response = requests.get(f"https://www.olx.pl/d/oferta/{self.name}.html")
        soup = BeautifulSoup(response.text, 'html.parser')
        self.title = soup.h1.text
        self.price = soup.find("div", {"data-testid": "ad-price-container"}).h3.text
        self.posted_at = soup.find("span", {"data-cy": "ad-posted-at"}).text

    def __repr__(self):
        return f"Title: {self.title}\nPrice: {self.price}\nPosted at: {self.posted_at}"


class OLXScrapper:
    offers: List[Offer]

    def __init__(self, links: List[str]):
        self.offers = [Offer(link) for link in links]

    def scrap(self):
        for i, offer in enumerate(self.offers):
            print(f"Scrapping offer no. {i + 1}")
            offer.scrap()

    def __repr__(self):
        return f'\n{"="*20}\n'.join([offer.__repr__() for offer in self.offers])


if __name__ == '__main__':
    offer_links = [
        'porsche-macan-salon-polska-przepiekny-braz-przejecie-leasing-CID5-IDMYzri.html',
        'komplet-dla-chlopca-czapka-i-komin-zimowy-niebieski-duet-48-50-CID88-IDN2q1k.html',
        'mercedes-e-klasa-w212-lift-2-2-cdi-2013r-automat-7-biegow-lub-zamiana-CID5-IDN1xch'
    ]

    olx_scrapper = OLXScrapper(offer_links)
    olx_scrapper.scrap()
    print()
    print(olx_scrapper)
