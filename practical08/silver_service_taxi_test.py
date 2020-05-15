from practical08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxi."""
    taxi = SilverServiceTaxi("Mostly Good", 100, 90)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()
