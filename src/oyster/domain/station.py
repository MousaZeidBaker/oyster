from enum import Enum
from typing import List

from pydantic import BaseModel


class Station(BaseModel):
    name: str
    zones: List[int]


class Stations(Enum):
    HOLBORN = Station(name="Holborn", zones=[1])
    ALDGATE = Station(name="Aldgate", zones=[1])
    EARLS_COURT = Station(name="Earl's Court", zones=[1, 2])
    HAMMERSMITH = Station(name="Hammersmith", zones=[2])
    ARSENAL = Station(name="Arsenal", zones=[2])
    WIMBLEDON = Station(name="Wimbledon", zones=[3])
