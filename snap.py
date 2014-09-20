import random

class Player(object):
    '''The player definition.'''
    
    def __init__(self, name):
        self.name = name
        self._points = 0
        
    @property
    def points(self):
        '''Cards owned.'''
        return self._points
    
    @points.setter
    def points(self, value):
        '''Set the earned cards counter.'''
        self._points = value
        
    @points.deleter
    def points(self):
        '''Delete counter.'''
        del self._points

    def __repr__(self):
        '''Print Player.'''
        return self.name
    
    def isWinner(self, other_player):
        '''Compare points.'''
        pass
    
class Card(object):
    '''The card definition.'''
    def __init__(self, suit, face_value):
        self.suit = suit
        self.face_value = face_value
        
    def __repr__(self):
        '''Print Card.'''
        return '{0} {1}'.format(self.suit, self.face_value)
    
    def isMatch(self, other_card):
        '''Compare Cards.'''
        pass

class SnapException(Exception):
    pass

class GameType:
    suit_match = 'suit'
    value_match = 'value'
    both_match = 'both'

class GameEngine(object):
    '''The game engine.'''
    def __init__(self, number_of_decks, game_type):
        
        if number_of_decks < 1:
            raise SnapException('Not valid number of decks.')
        
        self.deck = self.getDeck(number_of_decks)
        self.game_type = game_type
        
    def getDeck(self, number_of_decks):
        '''Return a shuffled deck of cards.'''
        
        #tuple uses less memory, and the number of elements is constant
        suits = ('spades', 'hearts', 'diamonds', 'clubs')
        face_values = ['A'] + [x for x in range(2, 11)] + ['J', 'Q', 'K']
        
        cards = []
        
        deck_counter = 0
        while (deck_counter < number_of_decks):
            for suit in suits:
                for face_value in face_values:
                    cards.append(Card(suit, face_value))
            deck_counter+=1
            
        # shuffle
        random.shuffle(cards)
        return cards

    def play(self, players):
        '''The frame of the game.'''
        
        played_cards = []
        
        # Loop until we have cards in the deck
        while(len(self.deck) > 1):
            
            # Picking cards
            actual_card = self.deck.pop()
            played_cards.append(actual_card)
            
            print 'The next card is : {0}'.format(actual_card)
            
            # Check match
            is_match = self.checkMatch(played_cards) if len(played_cards) > 1 else False
            
            # Increase points for the one who snapped
            if(is_match):
                winner_index = random.getrandbits(1)
                players[winner_index].points += len(played_cards)
                
                print '{0} says: SNAAAAAP!!!'.format(players[winner_index])
                
                #empty the played cards
                played_cards[:] = []
            
        
        self.announceTheWinner(players)
        
    def checkMatch(self, played_cards):
        '''Check if the last two cards are matching according to the game type.'''
        
        # get the last two played cards
        last_two_cards = played_cards[-2:]
        
        if self.game_type == 'suit':
            return last_two_cards[0].suit == last_two_cards[1].suit
        elif self.game_type == 'value':
            return last_two_cards[0].face_value == last_two_cards[1].face_value
        
        return (last_two_cards[0].suit == last_two_cards[1].suit and 
                last_two_cards[0].suit == last_two_cards[1].suit)
    
    def announceTheWinner(self, players):
        '''Announce the winner.'''
        
        if players[0].points == players[1].points:
            print 'Draw! {0}: {1} points, {2}: {3} points'.format(players[0], players[0].points, 
                                                                  players[1], players[1].points)
        else:
            # Put the winner at the first place
            players = sorted(players, key = lambda player: player.points, reverse = True)
            print '{0} is the winner! {1}: {2} points, {3}: {4} points'.format(players[0], players[0], 
                                                                               players[0].points, players[1], 
                                                                               players[1].points)

def main():
    player1 = Player('Jekyll')
    player2 = Player('Hyde')
    try:
        gameEngine = GameEngine(2, GameType.value_match)
        gameEngine.play((player1, player2))
    except SnapException as ex:
        print ex
    # A lot of more exception handling ...
    
if __name__ == "__main__":
    main()    
