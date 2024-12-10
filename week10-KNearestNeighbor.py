import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
print(iris.keys())

df = pd.DataFrame(iris['data'])
print(df)
print(iris['target_names'])
print(iris['feature_names'])
print(iris['target'])
x = df
y = iris['target']

from sklearn.neighbors import KNeighborsClassifier
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print("Correct prediction:",accuracy_score(y_test,y_pred))
print("Wrong prediction:",(1-accuracy_score(y_test,y_pred)))
y_test_train = knn.predict(x_train)
cm1 = confusion_matrix(y_train,y_test_train)
print(cm1)
      
