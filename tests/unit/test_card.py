import random

import pytest

from oyster.domain.card import Card, InsufficientBalance


def test_card_add():
    card = Card()
    amount = random.uniform(10, 50)
    card.add(amount)
    assert card.balance == amount


def test_card_deduct():
    card = Card(balance=100)
    amount = random.uniform(10, 50)
    card.deduct(amount)
    expected = 100 - amount
    assert card.balance == expected


def test_card_raises_insufficient_balance_exception_when_not_enough_balance():
    card = Card(balance=5)
    with pytest.raises(InsufficientBalance):
        card.deduct(10)
