import unittest
import numpy as np
import pandas as pd
from MonteCarloSimulator.die import Die
from MonteCarloSimulator.game import Game
from MonteCarloSimulator.analyzer import Analyzer

class TestDie(unittest.TestCase):
    def test_init_valid(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.assertIsInstance(die, Die)
    
    def test_change_weight(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        die.change_weight(1, 2.0)
        self.assertEqual(die.currState().loc[1, 'weight'], 2.0)
    
    def test_change_weight_invalid_value(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        with self.assertRaises(ValueError):
            die.change_weight(1, -1.0)

    def test_change_weight_invalid_type(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        with self.assertRaises(TypeError):
            die.change_weight(1, "invalid_weight")
    
    def test_roll_length(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        rolls = die.roll(10)
        self.assertEqual(len(rolls), 10)
    
    def test_currState(self):
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        state = die.currState()
        self.assertIsInstance(state, pd.DataFrame)
        self.assertEqual(state.shape, (6, 1))
    


class TestGame(unittest.TestCase):
    def test_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.assertIsInstance(self.game, Game)
        self.assertEqual(len(self.game.dice), 2)
        self.assertIsInstance(self.game.dice[0], Die)
    
    def test_play(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)
        self.assertEqual(len(self.game.game_results), 10)
        self.assertEqual(len(self.game.game_results.columns), 2)

    # test to ensure wide data frame
    def test_wide_frame(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)
        wide_df = self.game.show(format='wide')
        self.assertEqual(wide_df.index.name, 'roll')
        self.assertEqual(len(wide_df.columns), 2)

    def test_narrow_frame(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)
        narrow_df = self.game.show(format='narrow')
        self.assertEqual(narrow_df.index.names, ['roll', 'die'])
    
    def test_play(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)  
        self.assertIsInstance(self.game.game_results, pd.DataFrame)
        self.assertEqual(self.game.game_results.shape, (10, 2))

    def test_show(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)
        wide_df = self.game.show(format='wide')
        narrow_df = self.game.show(format='narrow')
        self.assertIsInstance(wide_df, pd.DataFrame)
        self.assertIsInstance(narrow_df, pd.Series)

class TestAnalyzer(unittest.TestCase):
    def test_jackpot_with_jackpot(self):    
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        game.game_results = pd.DataFrame({
        0: [1, 2, 3, 4],  # die0 results
        1: [1, 5, 3, 6]   # die1 results
        })
        game.game_results.index.name = 'roll'

        analyzer = Analyzer(game)

        self.assertEqual(analyzer.jackpot(), 2)

    def test_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        game.play(10)
        analyzer = Analyzer(game)

        self.assertIsInstance(analyzer, Analyzer)
    
    def test_face_counts_per_roll_shape(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        game.play(10)
        analyzer = Analyzer(game)

        self.assertEqual(analyzer.face_counts_per_roll().shape[0], 10)

    def test_counts_per_roll(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        
        game.game_results = pd.DataFrame({
            # each index in a row is a roll
            0: [1, 3, 3, 4],  # this is die 0
            1: [1, 5, 3, 6],  # htis is diwe 1
        })
        game.game_results.index.name = 'roll'
        analyzer = Analyzer(game)

        result = analyzer.face_counts_per_roll()

        expected = result.loc[2,3]
        self.assertEqual(expected, 2)

        

    def test_combination_counts(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        
        game.game_results = pd.DataFrame({
            0: [1, 2, 1, 2],  
            1: [1, 5, 2, 1],  
        })
        game.game_results.index.name = 'roll'
        analyzer = Analyzer(game)

        expected = pd.DataFrame(
            data=[[1], [1], [2]],
            index=[(1,1), (2,5), (1,2)],
            columns=['count']
        )
        expected.index.name = 'combination'

        result = analyzer.combination_counts()
        self.assertTrue(result.equals(expected))
        
        
    def test_permutations_counts(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        
        game.game_results = pd.DataFrame({
            0: [1, 2, 1, 2],  
            1: [1, 5, 2, 1],   
        })
        game.game_results.index.name = 'roll'
        analyzer = Analyzer(game)

        expected = pd.DataFrame(
            data=[[1], [1], [1], [1]],
            index=[(1,1), (2,5), (1,2), (2,1)],
            columns=['count']
        )
        expected.index.name = 'permutation'

        result = analyzer.permutation_counts()
        self.assertTrue(result.equals(expected))
        