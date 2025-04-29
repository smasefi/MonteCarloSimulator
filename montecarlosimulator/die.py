import numpy as np
import pandas as pd
from MonteCarloSimulator.die import Die
from MonteCarloSimulator.game import Game
from MonteCarloSimulator.analyzer import Analyzer

class Die:
    '''
    This class is representative of a die object. It contains 4 methods. The die method replicates 
    the behavior of a dice.

    1. __init__: This method initializes the die object with a list of faces and an optional weight.
    2. change_weight: This method allows the user to change the weight of a specific face on the die.
    3. roll: This method simulates rolling the die a specified number of times and returns the results.
    4. currState: This method returns the current state of the die, including the faces and their weights.
    '''

    def __init__(self, faces, weight=None):
        '''
        This method initializes the die object with a list of faces and an optional weight. It replicates
        what a die would look like by taking in a list of integers or strings and an optional weight. The weight
        would change the likelihood that a particular face is chosen. Creates a private die data frame.

        :param faces: list of integers or strings
        :param weight: list of floats (optional)
        :return: None
        '''
        # check to make sure the type is a numpy array
        if not isinstance(faces, np.ndarray):
            raise TypeError("faces must be a numpy array")
        
        # check to make sure the array's data type is a string or int
        if not (np.issubdtype(faces.dtype, np.integer) or np.issubdtype(faces.dtype, np.str_)):
            raise TypeError("faces must be a list of integers or strings")
        
        # check if array values are unique
        if len(faces) != len(np.unique(faces)):
            raise ValueError("faces must be unique")
        
        # set weight to be an array of ones
        weight = [1.0]*len(faces)
        # save both face and weight to a private data frame
        self._die = pd.DataFrame(
            {
                'weight': weight
            }, index=faces
        )


    def change_weight(self, face, weight):
        '''
        This method allows the user to change the weight of a specific face on the die. Based on the 
        position of the face, a user of this game is able to change or alter the specific weights.
        :param face: integer or string of face value
        :param weight: float
        :return: None
        '''
        # check to see if face is in the die
        if face not in self._die.index:
            raise IndexError("face not in die")
        
        # Checks to see if the weight is a valid type, i.e. if it is numeric
        #(integer or float) or castable as numeric. If not, raises a
        #`TypeError`.
        #if weight != int(weight) or weight != float(weight):
            #raise TypeError("weight must be a float or an int")
        if not isinstance(weight, (int, float)):
            raise TypeError("weight must be a float or an int")
        # check to make sure weight is positive or greater than zero
        if weight < 0:
            raise ValueError("weight must be equal to 0 or positive")
        
        # TODO: need to write code to change the weight for alloted face
        self._die.loc[face, 'weight'] = weight
        # Updated the weight for the specified face

    def roll(self, n=1):
        '''
        This method simulates rolling the die a specified number of times and returns the results of the roll.
        The default number of rolls is one, so if nothing is passed in, it will roll once. 
        :param n: integer value for number of rolls
        :return: list of outcomes
        '''
        # TODO: random sample with replacement from private data frame that applies weights
        rolls = np.random.choice(self._die.index, size=n, p=self._die['weight']/self._die['weight'].sum())
        # TODO: Returns list of outcomes
        rolls = rolls.tolist()
        return rolls

    def currState(self):
        '''
        This method returns the current state of the die, including the faces and their weights. It just returns a 
        copy in the event that the user wants to change the die state. The copy is a deep copy, so it won't affect the original.
        :param: None
        :return: private DataFrame of die state
        '''
        #TODO: Returns the current state of the die
        return self._die.copy()
    
