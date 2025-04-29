import numpy as np
import pandas as pd
from die import Die
from game import Game

class Analyzer:
    '''
    This class is the analyzer class and contains 5 methods. This class takes the results of a single game
    and computes various descriptive statistical properties to talk about.

    1. __init__: Takes the game object as a parameter and will have an error if it is not the game 
    object
    2. jackpot: This method counts the number of times a jackpot occurs in the game results.
    3. face_counts_per_roll: This method counts the number of times each face appears in each roll.
    4. combination_counts: This method counts the number of times each combination of faces appears in the game results.
    5. permutation_counts: This method counts the number of times each permutation of faces appears in the game results.
    '''

    def __init__(self, gameval):
        '''
        This method initializes the analyzer object with a game object. 
        :param gameval: Game object
        :return: Value Error if the gameval is not a game object
        :return: None
        '''
        if not isinstance(gameval, Game):
            return ValueError("gameval must be a Game object")
        self.gameval = gameval
        self._game_results = gameval.show(format='wide')

    def jackpot(self):
        '''
        This method counts the number of times a jackpot occurs in the game results.
        :return: integer for the number of jackpots
        '''
        jackpot_count = 0
        for i in range(len(self._game_results)):
            if len(set(self._game_results.iloc[i])) == 1: #sets check if the values are unique
                jackpot_count += 1
        return jackpot_count    
    
    def face_counts_per_roll(self):
        '''
        This method counts the number of times each face appears in each roll. Computes how many times a given face
        is rolled for each roll.
        :return: DataFrame of face counts
        '''
        counts = self._game_results.apply(pd.Series.value_counts, axis=1) # go down df
        # make sure this is formatted wide in testing
        return counts
    
    #order does not matter of the faces that show per roll
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
    def combination_counts(self):
        '''
        This method computes the number of distinct combinations that appear within a roll, along with 
        their counts. A combination isn't privvy to order, so it doesn't matter what the order of 
        the given faces are within a roll.
        :param game: None
        :return: DataFrame of combination counts
        '''
        counts = {}
        for index, row in self._game_results.iterrows():
            combination = tuple(sorted(row))
            if combination in counts:
                counts[combination] += 1
            else:
                counts[combination] = 1
        combinations = pd.DataFrame.from_dict(counts, orient='index', columns=['count'])
        combinations.index.name = 'combination'
        return combinations
    
    # order does matter of the faces that show per roll
    def permutation_counts(self):
        '''
        This method computes the number of distinct permutations that appear within a roll, along with
        their counts. A permutation is privvy to order, so it does matter what the order of
        the given faces are within a roll.
        :param game: None
        :return: DataFrame of permutation counts
        '''
        counts = {}
        for index, row in self._game_results.iterrows():
            permutations = tuple(row)
            if permutations in counts:
                counts[permutations] += 1
            else:
                counts[permutations] = 1
        perm = pd.DataFrame.from_dict(counts, orient='index', columns=['count'])
        perm.index.name = 'permutation'
        return perm

    

    
