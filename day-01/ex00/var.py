
class MyClass:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        return f"{self.value} has a type {self.type}"

obj = MyClass(42, type(42))
print(obj)

obj = MyClass("42", type("42"))
print(obj)

obj = MyClass("42", type("42"))
print(obj)

obj = MyClass(42.0, type(42.0))
print(obj)

obj = MyClass(True, type(True))
print(obj)

obj = MyClass([42], type([42]))
print(obj)

obj = MyClass({42: 42}, type({42: 42}))
print(obj)

obj = MyClass((42,), type((42,)))
print(obj)

obj = MyClass(set(), type(set()))
print(obj)