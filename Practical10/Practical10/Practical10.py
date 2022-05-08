import math

class CountDown():

    def __init__(self, number):
        self.number = number

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        self.returnable = self.number
        self.number = self.number - 1
        return self.returnable

    def __iter__(self):
        return self

class PowerTwo():

    def __init__(self, noOfNumbers):
        self.noOfNumbers = noOfNumbers
        self.index = -1

    def __next__(self):
        self.index +=1
        if self.noOfNumbers == self.index:
            raise StopIteration
        return int(math.pow(2, self.index))

    def __iter__(self):
        return self



cd = CountDown(4)
for x in cd:
    print(x)

print("------------------")

powers = PowerTwo(6)
while True:
    try:
        print(next(powers))
    except StopIteration:
        break

print("---------------------")
celsius_t = [39.2, 36.5, 37.3, 37.8]

fahrenheit_t = [round(9/5*temperatures + 32, 5) for temperatures in celsius_t]
print(celsius_t, fahrenheit_t)
print("---------------------")

triplets = [[x,y,z] for x in range(30) for y in range(30) for z in range(30) if (math.pow(x,2) + math.pow(y,2) == math.pow(z,2)) and x!=0 and y!=0 and z!=0]
print(triplets)
print("-------------------------")

odd_numbers = [x for x in range(10, 100) if x%2 ==1]
print(odd_numbers)

print("------------------------")

spins = [('red', '18'), ('black', '13'), ('red', '7'),
 ('red', '5'), ('black', '13'), ('red', '25'),
 ('red', '9'), ('black', '26'), ('black', '15'),
 ('black', '20'), ('black', '31'), ('red', '3')]

def redspins(spins):
    redOccurence = 0
    for play in spins:
        if play[0] == 'red':
            redOccurence +=1
        else:
            yield redOccurence
            redOccurence=0

redSpinCount = [redOccurence for redOccurence in redspins(spins)]
print(redSpinCount)
    
