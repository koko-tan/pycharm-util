from sklearn import datasets


irs = datasets.load_iris()
digits = datasets.load_digits()

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])