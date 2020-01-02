import unittest

from app.blackjack import BlackJack
from app.cards import Card, Ace, Two, Eight


class TestBlackJack(unittest.TestCase):

    def test_method_get_card_in_deck_should_be_return_obj_card(self):
        blackjack = BlackJack()
        self.assertIsInstance(blackjack.get_card_in_deck(), Card)

    def test_calc_player_points_with_first_card_is_ace_should_be_return_11(self):
        blackjack = BlackJack()
        ace = Ace()
        blackjack._player_cards.append(ace)
        self.assertEqual(11, blackjack.calc_player_points())

    def test_calc_player_points_should_be_return_sum_of_cards_values(self):
        blackjack = BlackJack()
        blackjack._player_cards.append(Two())
        blackjack._player_cards.append(Eight())
        self.assertEqual(10, blackjack.calc_player_points())

    def test_method_has_21_points_should_be_return_true_or_false(self):
        blackjack = BlackJack()
        self.assertFalse(blackjack.has_21_points())
        blackjack._points = 21
        self.assertTrue(blackjack.has_21_points())
