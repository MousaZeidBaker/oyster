import uuid

from pydantic import BaseModel


class InsufficientBalance(Exception):
    pass


class Card(BaseModel):
    """Represents a card"""

    id: str = uuid.uuid4()
    balance: float = 0.0

    def add(self, amount: float) -> None:
        """Add amount to balance."""

        self.balance = self.balance + amount

    def deduct(self, amount: float) -> None:
        """Deduct amount from balance."""

        if amount > self.balance:
            raise InsufficientBalance
        self.balance = self.balance - amount
