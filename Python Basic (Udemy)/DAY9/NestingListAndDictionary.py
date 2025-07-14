capitals = {
    # key :  value
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travelLog = {
    "France": ["Pairs", "Lille", "Dijon"],
    "Germany": ["berlin", "Hamburg", "Stuttgart"],
    "India": "Delhi",
}

#Nesting dictionary in a Dictionary
travelLog = {
    "France": {
        "CitiesVisited": ["Paris", "Lille", "Dijon"],
        "TotalVisit": 12,
    },
    "Germany": {
        "citiesVisited": ["Berlin", "Hamburg", "Stuttgart"],
        "TotalVisit": 5,
    },
}

#Nesting Dictionary in a List
travelLog = [
    {   
        "Country": "France",
        "CitiesVisited": ["Paris", "Lille", "Dijon"],
        "TotalVisit": 12,
    },
    {   
        "Country": "Germany",
        "citiesVisited": ["Berlin", "Hamburg", "Stuttgart"],
        "TotalVisit": 5,
    },
]