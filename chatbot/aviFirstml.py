from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as mp
from sklearn.model_selection import train_test_split
iris_dataset=load_iris()
X_t,x_t,Y_t,y_t=train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0)
kn=KNeighborsClassifier(n_neighbors=1)
kn.fit(X_t,Y_t)
x_new=mp.array([[5,2.9,1,0.2]])
prediction=kn.predict(x_new)
print("Predicted target value: {}\n".format(prediction))
print("Predicted feature name: {}\n".format
    (iris_dataset["target_names"][prediction]))
print("Test score: {:.2f}".format(kn.score(X_t,Y_t)))