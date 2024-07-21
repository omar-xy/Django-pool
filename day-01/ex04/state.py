import sys

class CapitalCity:
    def __init__(self, input, states, capital_cities):
        self.input = input
        self.states = states
        self.capital_cities = capital_cities

    def get_state(self, input):
        for i in self.states.keys():
            if input == i:
                return self.states[input]
        return None
    
    def get_city(self, input):
        for key, value in self.capital_cities.items():
            if input == value:
                return key
        return None

    def findbystate(self, state):
        if state in self.capital_cities.keys():
            return capital_cities[state]
        return None

    def findbycity(self, city):
        for key, value in self.states.items():
            if city == value:
                return key

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if len(sys.argv) != 3:
    input = sys.argv[1]
    obj = CapitalCity(input, states, capital_cities)
    city = obj.get_city(input)
    state = obj.findbycity(city)
    if state == None:
        print("Unknown city")
    else:
        print(state)