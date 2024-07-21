import sys


class CapitalCity:
    def __init__(self, states, capital_cities):
        self.states = states
        self.capital_cities = capital_cities

    def get_state(self, input):
        for key, value in self.states.items():
            if input == key:
                return value
        return None
    
    def get_city(self, input):
        for key, value in self.capital_cities.items():
            if input == value:
                return key
        return None

    def findbystate(self, state):
        for key, value in self.capital_cities.items():
            if state == key:
                return value
        return None

    def findbycity(self, city):
        for key, value in self.states.items():
            if city == value:
                return key


def capitalize_first_letter(s):
    return s.capitalize()

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
    obj = CapitalCity(states, capital_cities)
    tokens = input.split(',')
    for i in tokens:
        capitalized = capitalize_first_letter(i)
        i = capitalized.strip()
        if i:
            midkey = obj.get_state(i)
            city = obj.findbystate(midkey)
            if city == None:
                print(f"{i} is neither a capital city nor a state")
            else:
                print(f"{city} is the capital of {i}")

