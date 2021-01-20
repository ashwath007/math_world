


class ev():
    def __init__(self,y_pred,y,status=True):
        self.y_pred = y_pred
        self.y = y
    def MSE(self):
        sum_ar = []
        if(len(self.y_pred) == len(self.y)):
            for i in range(len(self.y_pred)):
                sum_ar.append((self.y_pred[i] - self.y[i])**2)
            return sum(sum_ar)/len(self.y_pred)
        else:
            return "Provide y^ and y of same dimentions"



