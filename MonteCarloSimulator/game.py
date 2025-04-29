import numpy as np
import pandas as pd
from die import Die

class Game:
    '''
    This class is representative of what a game of dice would consist of and has 3 methods. Takes the 
    die objects and has the actions that would be taken by a game. This class has methods that exhibit
    behaviors of a game. 

    1. __init__: This method initializes the game object with a list of die objects.
    2. play: This method simulates rolling the dice a specified number of times and returns the results.
    3. show: This method returns the results of the game in either wide or narrow format depending on what
    is being entered.
    '''
    def __init__(self, dice):
        '''
        This method initializes the game object with a list of die objects.
        :param dice: list of Die objects
        :return: None
        '''
        # each dice has a face and weight association via the die object --> this is a list of dice
        #TODO: checks to make sure they all have the same number of faces

        #TODO: checks list to make sure it contains Die objects
        self.dice = dice
        self._game_results = None

    def play(self, num_rolls):
        '''
        This method takes in the number of rolls that should be played on a set of dice
        and saves the results of the rolls in a private data frame.

        :param num_rolls: integer
        :return: None
        '''
        #TODO: take the integer and call the roll method
        results = {}
        for i, die in enumerate(self.dice):
            # add the roll results into the results frame
            results[i] = [die.roll()[0] for _ in range(num_rolls)]
        # should be in wide format
        #TODO: Save results to a private data frame
        self._game_results = pd.DataFrame(results) 
        self._game_results.index.name = 'roll' # make sure the index is the roll number
        self._game_results.unstack() # ensure that it is wide format

    def show(self, format='wide'):
        '''
        The show method returns the game results in either wide or narrow format depending on 
        what it is passed as an argument. The default is wide.

        :param format: 'wide' or 'narrow'
        :return: private DataFrame of game results
        '''
        if format == 'wide':
            return self._game_results.copy()
        elif format == 'narrow':
            narrow = self._game_results.stack()
            narrow.index.names = ['roll', 'die']
            return narrow
        else:
            raise ValueError("format must be either wide or narrow")