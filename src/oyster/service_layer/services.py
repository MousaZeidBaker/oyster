from typing import List

from oyster.domain.card import Card
from oyster.domain.trip import Trip


def make_trips(card: Card, trips: List[Trip]) -> None:
    for trip in trips:
        card.deduct(trip.calculate_price())
