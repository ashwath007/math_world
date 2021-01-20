import hell as H


y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

c = H.ev(y_true,y_pred)
print(c.MSE())