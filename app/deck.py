import random

from app.cards import Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, K, Q, J


class Deck:

    _cards = [
        Ace(),
        Two(),
        Three(),
        Four(),
        Five(),
        Six(),
        Seven(),
        Eight(),
        Nine(),
        Ten(),
        K(),
        Q(),
        J(),
    ]

    def shuffle_deck(self):
        random.shuffle(self._cards)
