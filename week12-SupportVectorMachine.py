from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
cancer = load_breast_cancer()
x = cancer.data[:, :2]
y = cancer.target

svm = SVC(kernel="rbf", gamma=0.5, C=1.0)
svm.fit(x, y)

DecisionBoundaryDisplay.from_estimator(
    svm,
    x,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel=cancer.feature_names[0],
    ylabel=cancer.feature_names[1]
)

plt.scatter(x[:, 0], x[:, 1],
            c=y,
            s=20, edgecolors="k")
plt.show()
