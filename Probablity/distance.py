from math import sqrt



class distance():
    def __init__(self,x):
        self.x = x
    def euclidean():
        if len(self.x) ==2:
            X = self.x[0]
            Y = self.x[1]
            return sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)
        else:
            return "Please provide correct dimention"


dis = distance([[0,1],[1,1]])
print(dis.euclidean())
