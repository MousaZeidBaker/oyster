from oyster.domain.station import Station, Stations
from oyster.domain.trip import Price, Trip, TripType


def test_trip_price_when_type_is_bus():
    trip = Trip(
        type=TripType.BUS,
        start_station=Stations.HOLBORN.value,
        end_station=Station(name="Chelsea", zones=[]),
    )
    assert trip.calculate_price() == Price.BUS.value


def test_trip_price_when_trip_not_finished():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.HOLBORN.value,
    )
    assert trip.calculate_price() == Price.MAX.value


def test_trip_price_when_one_zone_in_zone_1():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.HOLBORN.value,
        end_station=Stations.ALDGATE.value,
    )
    assert trip.calculate_price() == Price.ONE_ZONE_IN_ZONE_1.value


def test_trip_price_when_one_zone_outside_zone_1():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.ARSENAL.value,
        end_station=Stations.HAMMERSMITH.value,
    )
    assert trip.calculate_price() == Price.ONE_ZONE_OUTSIDE_ZONE_1.value


def test_trip_price_when_two_zones_including_zone_1():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.HAMMERSMITH.value,
        end_station=Stations.HOLBORN.value,
    )
    assert trip.calculate_price() == Price.TWO_ZONES_INCLUDING_ZONE_1.value


def test_trip_price_when_two_zones_excluding_zone_1():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.ARSENAL.value,
        end_station=Stations.WIMBLEDON.value,
    )
    assert trip.calculate_price() == Price.TWO_ZONES_EXCLUDING_ZONE_1.value


def test_trip_price_when_more_than_two_zones():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.WIMBLEDON.value,
        end_station=Stations.ALDGATE.value,
    )
    assert trip.calculate_price() == Price.MAX.value


def test_trip_price_is_lowest_when_more_than_one_price_possible():
    trip = Trip(
        type=TripType.TUBE,
        start_station=Stations.HOLBORN.value,
        end_station=Stations.EARLS_COURT.value,
    )
    assert trip.calculate_price() == 2.50
