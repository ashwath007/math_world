import hell as H
# import distance as d
from distance import manhattan2d,euclidean2d

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
s=False
c = H.ev(y_true,y_pred,s)
print(c.MSE())


# dis = d.distance([[10,12],[20,24],[15,18],[10,8],[5,7]])
# dis1 = d.distance([[2, 3], [5, 6]])
# dd = d.distance()
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
print(euclidean2d(row1, row2))
# print(manhattan2d(row1, row2))