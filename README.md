# Monte Carlo Simulator
Metadata:
    Name: Samantha Asefi
    Project Name: Monte Carlo Simulator

Synopsis:
How to install the code:
Step 1: Run command - python setup.py install
```
python3 setup.py install
```
Step 2: Run command - pip install .
```
pip install .
```
Step 3: Make sure the code is up to date and run the tests
```
python3 -m unittest test.py
```
Step 4: Create a python file play_game.py and import the following at the top
```
from montecarlosimulator.die import Die
from montecarlosimulator.game import Game
from montecarlosimulator.analyzer import Analyzer

```
Step 5: Create Dice - in this example there are 2 dice and changes of weights making certain faces way more likely to be rolled than others. The face 6 - is five times more likely to be rolled than other faces. The face 4 in the second die is 3 times more likely to be rolled than the others.
```
faces1 = np.array([1, 2, 3, 4, 5, 6])
faces2= np.array([2, 4, 6, 8, 10, 12])
die1 = Die(faces1)
die2 = Die(faces2)

die1.change_weight(6, 5.0)
die2.change_weight(4, 3.0)
```
Step 6: Play a game and play it 5 times
```
game = Game([die1, die2])
game.play(5)

print(game.show())
```
Step 7: Analyze the game
```
analyzer = Analyzer(game)
print(analyzer.jackpot())
print(analyzer.face_counts_per_roll())
print(analyzer.combination_counts())
print(analyzer.permutation_counts())


```

API description: 
Die Class:
    ```
    '''
    This class is representative of a die object. It contains 4 methods. The die method replicates 
    the behavior of a die and it has N number of faces and has adjustable weights assigned to it.

    1. __init__: This method initializes the die object with a list of faces and an optional weight.
    2. change_weight: This method allows the user to change the weight of a specific face on the die.
    3. roll: This method simulates rolling the die a specified number of times and returns the results.
    4. currState: This method returns the current state of the die, including the faces and their weights.
    '''

    def __init__(self, face, weight=None)
        '''
        This method initializes the die object with a list of faces and an optional weight. It replicates
        what a die would look like by taking in a list of integers or strings and an optional weight. The weight
        would change the likelihood that a particular face is chosen. Creates a private die data frame.

        :param faces: list of integers or strings
        :param weight: list of floats (optional)
        :return: None
        '''
    def change_weight(self, face, weight)
       '''
        This method allows the user to change the weight of a specific face on the die. Based on the 
        position of the face, a user of this game is able to change or alter the specific weights.
        :param face: integer or string of face value
        :param weight: float
        :return: None
        '''
    def roll(self, n=1):
        '''
        This method simulates rolling the die a specified number of times and returns the results of the roll.
        The default number of rolls is one, so if nothing is passed in, it will roll once. 
        :param n: integer value for number of rolls
        :return: list of outcomes
        '''
     def currState(self):
        '''
        This method returns the current state of the die, including the faces and their weights. It just returns a 
        copy in the event that the user wants to change the die state. The copy is a deep copy, so it won't affect the original.
        :param: None
        :return: private DataFrame of die state
        '''
    
    ```
Game Class
```
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
        
    def play(self, num_rolls):
        '''
        This method takes in the number of rolls that should be played on a set of dice
        and saves the results of the rolls in a private data frame.

        :param num_rolls: integer
        :return: None
        '''
    def show(self, format='wide'):
        '''
        The show method returns the game results in either wide or narrow format depending on 
        what it is passed as an argument. The default is wide.

        :param format: 'wide' or 'narrow'
        :return: private DataFrame of game results
        '''
```
Analyzer Class
```
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
    def jackpot(self):
        '''
        This method counts the number of times a jackpot occurs in the game results.
        :return: integer for the number of jackpots
        '''
        
    def face_counts_per_roll(self):
        '''
        This method counts the number of times each face appears in each roll. Computes how many times a given face
        is rolled for each roll.
        :return: DataFrame of face counts
        '''
        
    def combination_counts(self):
        '''
        This method computes the number of distinct combinations that appear within a roll, along with 
        their counts. A combination isn't privvy to order, so it doesn't matter what the order of 
        the given faces are within a roll.
        :param game: None
        :return: DataFrame of combination counts
        '''
        
    def permutation_counts(self):
        '''
        This method computes the number of distinct permutations that appear within a roll, along with
        their counts. A permutation is privvy to order, so it does matter what the order of
        the given faces are within a roll.
        :param game: None
        :return: DataFrame of permutation counts
        '''
```
