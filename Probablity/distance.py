from math import sqrt



class distance():
    def __init__(self,x):
        self.x = x
    def euclidean(self):
        if len(self.x) ==2:
            X = self.x[0]
            Y = self.x[1]
            return sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)
        else:
            return "Please provide correct dimention"
    def manhattan(self):
        if len(self.x) ==2:
            X = self.x[0]
            Y = self.x[1]
            return (abs((X[0]-Y[0])) + abs((X[1]-Y[1])))


#Test Class
dis = distance([[3,1],[2,1]])
dis1 = distance([[2, 3], [5, 6]])
print(dis.euclidean())
print(dis1.manhattan())
