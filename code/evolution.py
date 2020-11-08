import random


class evo:
    def __init__(self):
        self.chromolen = 11
        self.crossRate = 0.7
        self.mutRate = 25
        self.poolSize = 10
        self.currentpool = 0
        self.epoch = 20
        self.gen = 0
        self.n = 0

    def evolve(self):
        self.gen = 0
        pool = self.chromogenerator()
        self.currentpool = self.decodechromo()

    def reproducir(self, chromoA, chromoB):
        cut = random.randrange(0, 10)
        chromoD = chromoA.chromo_data[:cut]+chromoB.chromo_data[cut:]
        chromoF = chromoB.chromo_data[:cut]+chromoA.chromo_data[cut:]
        return chromoD, chromoF

    def mutate(self, chromo):
        mut = random.randrange(0, 10)
        chromo_data = chromo.chromo_data
        if chromo_data[mut] == "0":
            chromo_data = chromo_data[:mut] + '1' + chromo_data[mut+1:]
        else:
            chromo_data = chromo_data[:mut] + '0' + chromo_data[mut+1:]

        chromo.chromo_data = chromo_data

    def chromogenerator(self):
        chromo = []
        for i in range(self.poolSize):
            a = random.randrange(0, 2047)
            binary = bin(a).replace("0b", "")
            for i in range(self.chromolen - len(binary)):
                binary = "0" + binary
            chromo.append(binary)

        self.currentpool = chromo
        return chromo

    def decodechromo(self):
        chromosomas = []
        for c in self.currentpool:

            power = c[:6]
            angle = c[6:]
            power = int(power, 2)
            angle = int(angle, 2)/20.38
            chromosomas.append(chromosome(c, power, angle))

        return chromosomas

    def get_score(xmax, chromo):
        return chromo.get_score(xmax)

    def play_chromo(self):
        #print(self.currentpool[self.n].power, self.currentpool[self.n].angle)
        chromo = self.currentpool[self.n]

        return chromo.power, chromo.angle

    def setXmax(self, xmax):
        # print(self.currentpool[self.n].score)
        self.currentpool[self.n].set_score(xmax)
        print(self.n)
        self.n += 1
        if self.n == self.poolSize:
            self.n = 0
            self.gen += 1
            self.next_gen()

    def next_gen(self):
        scores = []
        for c in self.currentpool:
            scores.append(c.score)
            scores.sort()
            print("score = "+str(c.score))
            # chromosons
        print("-------------------")
        self.currentpool.sort(key=lambda x: x.score, reverse=False)
        mid = int(len(self.currentpool)/2)
        self.currentpool = self.currentpool[:mid+1]
        newpool = []

        for i in range(0, 5, 2):
            chromoA, chromoB = self.reproducir(
                self.currentpool[i], self.currentpool[i+1])
            newpool.append(chromoA)
            newpool.append(chromoB)

        for i in range(0, 3, 2):
            chromoA, chromoB = self.reproducir(
                self.currentpool[i], self.currentpool[i+2])
            newpool.append(chromoA)
            newpool.append(chromoB)

        self.currentpool = newpool
        self.currentpool = self.decodechromo()

        if random.randrange(0, 100) < self.mutRate:
            m = random.randrange(0, 9)
            self.mutate(self.currentpool[m])

    def get_gen(self):
        return self.gen


class chromosome:
    def __init__(self, chromo_data, power, angle):
        self.xmax = 0
        self.score = 0
        self.power = power
        self.angle = angle
        self.chromo_data = chromo_data

    def set_score(self, xmax):

        self.score = abs(700-xmax)
