import sys


class CapitalCity:
    def __init__(self, input, states, capital_cities):
        self.input = input
        self.states = states
        self.capital_cities = capital_cities


    # def get_state(self, city):
    #     for state, capital in self.capital_cities.items():
    #         if capital == city:
    #             return state
    #     return None

    # def get_city(self, state):
    #     return self.capital_cities.get(state)

    def findbystate(self, state):
        if state in self.states:
            return capital_cities[self.states[state]]
        else:
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
 


obj = CapitalCity(input, states, capital_cities)
findbystate(state)