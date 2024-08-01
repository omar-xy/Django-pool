

class Intern:
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
        self.name = name
        self.coffee = self.Coffee()
    def __str__(self):
        return self.name
    
    def work(self):
        raise ValueError("I’m just an intern, I can’t do that...")
    def make_coffe(self):
        return self.coffee
            
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."


try:
    without_name = Intern()
    print(without_name.__str__())
    name = Intern("Mark")
    print(name.__str__())
    cname = name.make_coffe()
    print(cname.__str__())
    without_name.work()
except ValueError as o:
    print(o)

