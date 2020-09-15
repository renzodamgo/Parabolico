import random


class evo:
    def __init__(self):
        self.chromolen = 11
        self.crossRate = 0.7
        self.mutRate = 0.001
        self.poolSize = 10
        self.currentpool = 0

    def evolve(self):
        gen = 0
        pool = chromogenerator()
        currentpool = pool

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
        for c in self.currentpool:
            print(c)
            power = c[:6]
            angle = c[6:]

            print("power :" + power + " " + str(int(power, 2)))
            print("angle : " + angle + "  " + str(int(angle, 2)/20.38))


class chromosome:
    def __init__(power, angle):
        self.xmax = 0
        self.score = 0
        self.power = power
        self.angle = angle

    def get_score(xmax):
        score = abs(700-xmax)
        return score


e = evo()
e.chromogenerator()
e.decodechromo()
