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


    def findbystate(self, state):
        if state in self.capital_cities.keys():
            return capital_cities[state]
        return None

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
    state = obj.get_state(input)
    city = obj.findbystate(state)
    if city == None:
        print("Unknown state")
    else:
        print(city)