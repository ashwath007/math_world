import math


class sum_of_error():
    def __init__(self,y_pred,y):
        self.y_pred = y_pred
        self.y = y
    def cal(self):
        sum_y = []
        for i in range(len(self.y_pred)):
            sum_y.append((self.y[i]-self.y_pred[i])**2)

        return sum(sum_y)//len(self.y_pred)

def main():
    c = sum_of_error([2,3,4],[4,5,6])
    print(c.cal())

if __name__ == '__main__':
    main()