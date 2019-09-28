import random
import collections

class Guitarstring:
    def __init__(self, frequency):
        self.f = frequency
        self.p = int(44100/self.f)
        self.list = [0.0] *self.p
        self.wavetable = collections.deque(self.list)

    def pluck(self):
        for i in range(self.p):
            self.wavetable[i] = random.uniform(-0.5, 0.5)

    def tick(self):
        temp = self.wavetable.popleft()
        Yn = 0.996*0.5*(temp +self.wavetable[0])
        self.wavetable.append(Yn)
        return Yn