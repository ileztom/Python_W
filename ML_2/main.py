import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import sklearn
from sklearn import datasets

diabetes = datasets.load_diabetes()
diabetes

df = pd.DataFrame(diabetes.data)
df.columns = diabetes.feature_names
df

df["diabetes_measure"] = diabetes.target
df.head()

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

bmi = X.iloc[:, 2]
bmi = bmi[:, np.newaxis]
Y = Y[:, np.newaxis]

from sklearn.leanar_model import LinearRegression

simple_lr = LinearRegression()
simple_lr = LinearRegression().fit(bmi, Y)
predicted_Y = simple_lr.predict(bmi)

plt.figure(figsize=(10, 6))
plt.scatter(bmi, Y)
plt.plot(bmi, predicted_Y, c = "r")
plt.title("Линия регрессии на точечной диаграмме")
plt.ylabel("Y")
plt.show()

from sklearn.model_selection import cross_val_score

mse = cross_val_score(simple_lr, bmi, Y, scoring= "neg_mean_squared_error", cv=10)
mse.mean()

multiple_lr = LinearRegression().fit(X, Y)

mse1 = cross_val_score(simple_lr, X, Y, scoring= "neg_mean_squared_error", cv=10)
mse1.mean()

multiple_lr_coeffs = multiple_lr.coef_[0]
multiple_lr_coeffs

feature_names = df.drop("diabetes_measure", axis = 1).columns

plt.figure(figsize=(10, 6))
plt.plot(range(len(multiple_lr_coeffs)), multiple_lr_coeffs)
plt.axhline(0, color="r", linestyle="solid")
plt.xticks(range(len(future_names)), feature_names, rolation = 50)
plt.title("Коэффициенты множественной линейной регрессии")
plt.ylabel("Коэффициент")
plt.xlabel("Признаки")
plt.show()

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

alpha_value = {"alpha": [0.01, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 1, 2, 3, 5, 8, 10, 20, 50, 100]}
ridge = GridSearchCV(Ridge(), alpha_value, scoring= "neg_mean_squared_error", cv=10)
print("Лучшее значение для альфа: ", ridge.fit(X, Y).best_params_)
print("Среднее значение: ", ridge.fit(X, Y).best_score_)

best_ridge_model = Ridge(alpha = 0.04)
best_ridge_coeffs = best_ridge_model.fit(X, Y).coef_

plt.figure(figsize=(10, 6))
plt.plot(range(len(future_names)), best_ridge_coeffs[0])
plt.axhline(0, color="r", linestyle="solid")
plt.xticks(range(len(future_names)), feature_names, rolation = 50)
plt.title("Ridge-регрессия")
plt.ylabel("Коэффициент")
plt.xlabel("Признаки")
plt.show()

from sklearn.linear_model import Lasso
lasso = GridSearchCV(Lasso(), alpha_values, scoring= "neg_mean_squared_error", cv=10)
print("Лучшее значение для Альфа", lasso.fit(X, Y).best_params_)
print("Среднее значение", lasso.fit(X, Y).best_score_)

best_lasso_model = Lasso(alpha = 0.06)
best_lasso_coeffs = best_lasso_model.fit(X, Y).corf_

plt.figure(figsize=(10, 6))
plt.plot(range(len(future_names)), best_lasso_coeffs[0])
plt.axhline(0, color="r", linestyle="solid")
plt.xticks(range(len(future_names)), feature_names, rolation = 50)
plt.title("Lasso-регрессия")
plt.ylabel("Коэффициент")
plt.xlabel("Признаки")
plt.show()

