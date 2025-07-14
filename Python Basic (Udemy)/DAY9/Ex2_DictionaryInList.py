#List of Dictionary
travelLog = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def addNewCountry(countryVisited, timesVisited, citiesVisited) :
    # newCountry = {
    #     "country": countryVisited,
    #     "visits": timesVisited,
    #     "cities": citiesVisited,
    # }
    #****************OR******************
    newCountry = {}
    newCountry["country"] = countryVisited
    newCountry["visits"] = timesVisited
    newCountry["cities"] = citiesVisited
    travelLog.append(newCountry)

addNewCountry("Russia", 2, ["Moscow", "Sanit Petersburg"])
print(travelLog)