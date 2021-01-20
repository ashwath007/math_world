from math import sqrt


class ev():
    def __init__(self,y_pred,y,*RMSE):
        self.y_pred = y_pred
        self.y = y
        self.key = RMSE
        
    def MSE(self):
        sum_ar = []
        print(self.key[0])
        if(self.key[0]):
            if(len(self.y_pred) == len(self.y)):
                for i in range(len(self.y_pred)):
                    sum_ar.append((self.y_pred[i] - self.y[i])**2)
                return sum(sum_ar)/len(self.y_pred)
            else:
                raise Exception("Provide y^ and y of same dimentions") 
        else:
            if(len(self.y_pred) == len(self.y)):
                for i in range(len(self.y_pred)):
                    sum_ar.append((self.y_pred[i] - self.y[i])**2)
                return sqrt(sum(sum_ar)/len(self.y_pred))
            else:
                raise Exception("Provide y^ and y of same dimentions") 



