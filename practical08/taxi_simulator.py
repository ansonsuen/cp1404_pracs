from practical08.car import Car
from practical08.taxi import Taxi
from practical08.silver_service_taxi import SilverServiceTaxi


def menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_taxi(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{}-{}".format(i, taxi))


