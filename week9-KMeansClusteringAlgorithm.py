import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

iris = datasets.load_iris()
x = pd.DataFrame(iris.data)
x.columns = ['sepal_length','sepal_width','petal_length','petal_width']
y = pd.DataFrame(iris.target,columns=['target'])

plt.figure(figsize=(14,7))
colormap = np.array(['red','lime','black'])

plt.subplot(1,2,1)
plt.scatter(x.sepal_length,x.sepal_width,c=colormap[y.target],s=40)
plt.title('Sepal')

plt.subplot(1,2,2)
plt.scatter(x.petal_length,x.petal_width,c=colormap[y.target],s=40)
plt.title('Petal')

model = KMeans(n_clusters=3)
model.fit(x)
print(model.labels_)

plt.subplot(1,2,1)
plt.scatter(x.petal_length,x.petal_width,c=colormap[y.target],s=40)
plt.title('Real Classification')

plt.subplot(1,2,2)
plt.scatter(x.petal_length,x.petal_width,c=model.labels_,s=40)
plt.title('KMeans Classification')
plt.show()
