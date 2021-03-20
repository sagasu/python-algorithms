class UndergroundSystem:

    def __init__(self):
        self.currently_checked_in = {}
        self.average_time = collections.defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        self.currently_checked_in[id] = (station_name, t)
        

    def checkOut(self, id: int, station_name: str, t: int) -> None:
        if id in self.currently_checked_in:
            previous_station_name, previous_time = self.currently_checked_in[id]

            frac = self.average_time[(previous_station_name, station_name)]
            new_frac = (frac[0] + t - previous_time, frac[1] + 1)

            self.average_time[(previous_station_name, station_name)] = new_frac

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        frac = self.average_time[(start_station, end_station)]
        return frac[0] / frac[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)