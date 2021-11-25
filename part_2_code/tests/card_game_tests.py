import unittest
from src.card_game import CardGame
from src.card import Card

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace_true(self):
        ace_of_hearts = Card("heart", 1)
        eight_of_spades = Card("spade", 8)
        game = CardGame(ace_of_hearts, eight_of_spades)
        self.assertEqual(game.check_for_ace(ace_of_hearts), True)
        
    def test_check_for_ace_false(self):
        ace_of_hearts = Card("heart", 1)
        eight_of_spades = Card("spade", 8)
        game = CardGame(ace_of_hearts, eight_of_spades)
        self.assertEqual(game.check_for_ace(eight_of_spades), False)
        
    def test_highest_card_card1(self):
        ace_of_hearts = Card("heart", 1)
        eight_of_spades = Card("spade", 8)
        game = CardGame(ace_of_hearts, eight_of_spades)
        self.assertEqual(game.highest_card(eight_of_spades, ace_of_hearts), eight_of_spades)
        
    def test_highest_card_card2(self):
        ace_of_hearts = Card("heart", 1)
        eight_of_spades = Card("spade", 8)
        game = CardGame(ace_of_hearts, eight_of_spades)
        self.assertEqual(game.highest_card(ace_of_hearts, eight_of_spades), eight_of_spades)
        
    def test_cards_total(self):
        ace_of_hearts = Card("heart", 1)
        eight_of_spades = Card("spade", 8)
        cards_list = [ace_of_hearts, eight_of_spades]
        game = CardGame(ace_of_hearts, eight_of_spades)
        self.assertEqual(game.cards_total(cards_list), "You have a total of 9")