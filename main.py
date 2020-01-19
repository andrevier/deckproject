#main project file
from classes.deck import Tarot
from classes.deck import Deck

if __name__ == "__main__":
    mydeck = Tarot()

    for i in range(0,4):
        print(mydeck.deal())

    del mydeck

    print('-----------')
    mydeck = Deck()
    for i in range(0,4):
        print(mydeck.deal())

    del mydeck
