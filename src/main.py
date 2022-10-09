from oyster.domain.card import Card
from oyster.domain.station import Station, Stations
from oyster.domain.trip import Trip, TripType
from oyster.service_layer import services

if __name__ == "__main__":
    # create card and load it
    card = Card(balance=30)
    print(f"Balance before trips: {card.balance}")

    # create trips
    trip_a = Trip(
        type=TripType.TUBE,
        start_station=Stations.HOLBORN.value,
        end_station=Stations.EARLS_COURT.value,
    )
    trip_b = Trip(
        type=TripType.BUS,
        start_station=Stations.EARLS_COURT.value,
        end_station=Station(name="Chelsea", zones=[]),
    )
    trip_c = Trip(
        type=TripType.TUBE,
        start_station=Stations.EARLS_COURT.value,
        end_station=Stations.HAMMERSMITH.value,
    )
    services.make_trips(card, [trip_a, trip_b, trip_c])

    print(f"Balance after trips: {card.balance}")
