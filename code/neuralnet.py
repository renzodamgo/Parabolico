#Perceptron simple

class SimplePerceptron():
    def __init__(self,x1s,x2s,dXs):
        self.w1 = 1
        self.w2 = 1
        self.theta = 0.5
        self.x1s = x1s
        self.x2s = x2s
        self.dXs = dXs

    def train(self):
        
        for i in range(len(self.x1s)):
            while(True):
                fx = self.function(self.x1s[i],self.x2s[i])
                print(fx)
                if fx > 0 :
                    y = 1
                else:
                    y = -1
                print("Iteracion",i, "||||| x1: ",self.x1s[i]," x2: ",self.x2s[i],"dx", self.dXs[i]," w1: ",self.w1," w2: ",self.w2," theta: ",self.theta)


                if y == self.dXs[i]:
                    print("fucniona")
                    break
                else:
                    print("no funciona")
                    self.updateW(self.x1s[i],self.x2s[i],self.dXs[i])

    def function(self,x1,x2):
        fx = (x1*self.w1) + (x2*self.w2) + self.theta
        return fx

    def updateW(self,x1,x2,dx):
        self.w1 = self.w1 + dx * x1
        self.w2 = self.w2 + dx * x2
        self.theta = self.theta + dx
    
    def predict(x1,x2):
        return function(x1,x2)



ga = SimplePerceptron([-1,1,-1,1],[-1,-1,1,1],[-1,-1,-1,1])
ga.train()