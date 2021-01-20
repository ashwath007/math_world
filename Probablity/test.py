import hell as H


y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
s=False
c = H.ev(y_true,y_pred,s)
print(c.MSE())