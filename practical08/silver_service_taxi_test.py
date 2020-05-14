from practical08.silver_service_taxi import Silver_Service_Taxi


def main():
    """Test Silver Service Taxi."""
    taxi = Silver_Service_Taxi("Mostly Good", 100, 90)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()
