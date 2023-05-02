travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Poland", 1, ["Warsaw", "Krakow"])
add_new_country("Ukraine", 1, ["Kiev"])
add_new_country("Belarus", 1, ["Minsk"])
add_new_country("Lithuania", 1, ["Vilnius"])
add_new_country("Latvia", 1, ["Riga"])
add_new_country("Estonia", 1, ["Tallinn"])
add_new_country("Finland", 1, ["Helsinki"])

for country in travel_log:
    print(country)
