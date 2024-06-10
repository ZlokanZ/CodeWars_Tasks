def number(bus_stops):

    StopsLen = len(bus_stops)
    BusEntry = 0
    BusOut = 0
    while StopsLen != 0:
        BusEntry += bus_stops[StopsLen-1][0]
        BusOut += bus_stops[StopsLen-1][1]
        StopsLen-= 1
    return BusEntry - BusOut