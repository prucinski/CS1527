
class Counter:

    all_counters = []
    def __init__(self, initializationValue, i = 1):
        self._initial = initializationValue
        self._i = i
        self._numberOfCalls = 0
        Counter.all_counters.append(self)
    def increment(self):
        self.initial = self.initial + i
        _numberOfCalls+=1
    
    def decrement(self):
        self.initial = self.initial - i
        _numberOfCalls+=1

    def listCounters(cls):
        print("There are ", len(cls.all_counters), " counters currently initialized")
        for x in cls.all_counters:
            print(x)
    
    def __str__(self):
        return "Counter initialized with value "+ str(self._initial) + " has an increment of " + str(self._i) + " and has been called " + str(self._numberOfCalls) + " times"
    


counter1 = Counter(12)
counter2 = Counter (0, 2)
Counter.listCounters(Counter)