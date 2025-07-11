from abc import ABC, abstractmethod

class Charging_Station(ABC):
    def __init__(self, station_id, capacity, vehicles_served):
        self.station_id = station_id
        self.capacity = capacity    #cap per day (24 hours(seconds))
        self.vehicles_served = vehicles_served

    @abstractmethod
    def charge_hour():
        pass

class Lvl2_Charging_Station(Charging_Station):
    def __init__(self, station_id, capacity, vehicles_served):
        super().__init__(station_id, vehicles_served, capacity=40)

    def charge_hour(self, hours):
        for hour in hours:
            cost = .11 * 40


class lvl3_Charging_Station(Charging_Station):
    def __init__(self, station_id, vehicles_served, capacity):
        super().__init__(station_id, vehicles_served, capacity=80)

    def charge_hour(self, hours):
        for hour in hours:
            cost = .11 * 80

class Ev(ABC):
    def __init__(self, battery, cap_per_hour, rate):
        self.battery = battery
        self.cap_per_hour = cap_per_hour    #max cap per hour
        self.rate = rate    #rate per hour(second in sim)

    @abstractmethod
    def charge():
        pass

class Lvl2_Ev(Ev):
    def __init__(self, battery, cap_per_hour, rate):
        super().__init__(battery, cap_per_hour, rate)

    def charge():
        pass

class Lvl3_Ev(Ev):
    def __init__(self, battery, cap_per_hour, rate,):
        super().__init__(battery, cap_per_hour, rate)

    def charge(self):
        pass

class Community():
    def __init__(self, comm_id, num_vehicles, num_comm):
        self.comm_id = comm_id
        self.num_vehicles = num_vehicles
        self.num_comm = num_comm

    def assign_stations():
        pass
