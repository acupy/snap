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
