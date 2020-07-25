class Overload:
    def __init__(self, name):
        pass
    def __init__(self, name, age):
        pass
    
obj1 = Overload('joe', 37)
obj2 = Overload('scott')
