
class customException(Exception):
    def __init__(self, input, output = "wrong"):
        self.input = input
        self.output = output
        super().__init__(self.output)
    
    


a = input("Give a letter ")
if a != "a":
    raise customException(a)