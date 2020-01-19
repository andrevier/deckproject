#python oop card exercise
from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        ''' Returns the representation of the object '''
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        """ Class to represent the deck with normal cards. This fn also shuffles the deck. """
        self.cards = [Card(suit,value) for suit in Deck.suits for value in Deck.values] #big list of Card instances
        self.shuffle()

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled.')
        shuffle(self.cards)
        return self # return the object but shuffled.

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError('All cards have been dealt')
        return self.cards.pop()
    
    def __repr__(self):
        ''' shows the number of cards in the deck '''
        return "{} cards remaining in deck.".format(len(self.cards))
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values =['A','2', '3','4','5','6','7','8','9', '10', 'J','Q','K']

class Tarot:
    def __init__(self, decktype = 'all'):
        """ Class to deal Tarot cards in the deck. 
            This __init__ fn what the user wants: all deck (type all); Minor Arcana only (type minorarcana), Major arcana only (type majorarcana)
            This fn also shuffle the deck initially. """
        self.minorArcana = list()
        self.deck = list()
        self.minorArcana =["{} of {}".format(value,suit) for value in Tarot.values for suit in Tarot.suits]
        if decktype.upper() == 'MINORARCANA':
            self.deck = self.minorArcana            
        elif decktype.upper() =='MAJORARCANA':
            self.deck = self.majorArcana
        elif decktype.upper() == 'ALL':
            self.deck.extend(self.majorArcana)
            self.deck.extend(self.minorArcana)
        
        self.shuffle()

    def deal(self):
        """ Fn to deal the cards from the deck. Return a card. """
        if len(self.deck) == 0:
            raise ValueError('All cards have been dealt.')
        return self.deck.pop()

    def __repr__(self):
        '''shows the number of cards in the deck'''
        return "{} cards remaining in the deck.".format(len(self.deck))

    def shuffle(self):
        """ Fn to shuffle the deck unless it has no cards. """
        if len(self.deck) == 0:
            raise ValueError('no cards in the deck.')
        shuffle(self.deck)
        return 'deck is shuffled.'
        
    suits = ['Wands', 'Swords','Coins','Cups']
    values = ['Ace','2','3','4','5','6','7','8','9','10','Page','Knight','Queen','King']
    majorArcana = ['The Fool','The Magician','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The Star','The Moon','The Sun','Judgment','The World']
    

