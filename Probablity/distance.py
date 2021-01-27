from math import sqrt



class distance():
    def __init__(self,x=''):
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

def manhattan2d(a,b):
    return sum(abs(e1-e2) for e1,e2 in zip(a,b))
def euclidean2d(a,b):
    if isinstance(a[0], int) and isinstance(b[0], int):
        return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))   
    else:
        return "Try changing the dimention or use euclidean([[],[]]) function"

def hamming(a,b):
    return sum(abs(a-b) for a,b in zip(a,b))/len(a)


def euclideanD(X):
    res = list()
    for i in range(len(X)-1):
        print(X[i])
        for j in range(len(X[i])-1):
            res.append(sqrt(abs(X[i][j] - X[i+1][j])**2+abs(X[i][j+1] - X[i+1][j+1] )**2))
    return res


def help(self):
    print("Help section for Distance")
    return('''
        1. Euclidean distance - 
                    Use euclidean() function with parameter [[cord1,cord2]]
                                    
    ''')