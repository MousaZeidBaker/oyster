import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from oyster.domain.station import Station


class TripType(str, Enum):
    BUS = "BUS"
    TUBE = "TUBE"


class Price(float, Enum):
    BUS = 1.80
    MAX = 3.20
    ONE_ZONE_IN_ZONE_1 = 2.50
    ONE_ZONE_OUTSIDE_ZONE_1 = 2.00
    TWO_ZONES_INCLUDING_ZONE_1 = 3.00
    TWO_ZONES_EXCLUDING_ZONE_1 = 2.20


class Trip(BaseModel):
    """Represents a trip"""

    id: str = uuid.uuid4()
    type: TripType
    start_station: Station
    end_station: Optional[Station] = None

    def calculate_price(self) -> float:
        """Calculate trip price."""

        if self.type == TripType.BUS:
            # the price for a bus trip is fixed regardless of station
            return Price.BUS.value

        if self.end_station is None:
            # max price if end station not specified
            return Price.MAX.value

        # the price for a tube trip is based on the zones visited
        prices = [Price.MAX.value]
        for start_zone in self.start_station.zones:
            for end_zone in self.end_station.zones:
                nr_of_zones = abs(start_zone - end_zone) + 1
                is_zone_1 = start_zone == 1 or end_zone == 1
                if nr_of_zones == 1:
                    price = (
                        Price.ONE_ZONE_IN_ZONE_1.value
                        if is_zone_1
                        else Price.ONE_ZONE_OUTSIDE_ZONE_1.value
                    )
                elif nr_of_zones == 2:
                    price = (
                        Price.TWO_ZONES_INCLUDING_ZONE_1.value
                        if is_zone_1
                        else Price.TWO_ZONES_EXCLUDING_ZONE_1.value
                    )
                else:
                    # max price for trips with more than 2 zones
                    price = Price.MAX.value
                prices.append(price)
        return min(prices)  # return lowest price when more than one possible
