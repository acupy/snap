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
