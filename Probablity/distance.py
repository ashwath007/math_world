from math import sqrt



class distance():
    def __init__(self,x=''):
        self.x = x
    def euclidean2d(self,a,b):
        return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))   

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
dis = distance([[10,12],[20,24],[15,18],[10,8],[5,7]])
dis1 = distance([[2, 3], [5, 6]])
dd = distance()
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
print(dd.euclidean2d(row1, row2))
# print(dis1.manhattan())


# Todo : return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))