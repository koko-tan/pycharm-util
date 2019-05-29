from sklearn import datasets
from sklearn import linear_model
import matplotlib.pyplot as plt








def main():
    data = datasets.load_iris()
    dataX = data.data
    dataY = data.target
    plt.scatter(dataX[0:50,0], dataX[0:50,1], c='r')
    plt.scatter(dataX[50:100, 0], dataX[50:100, 1], c='g')
    plt.scatter(dataX[100:150, 0], dataX[100:150, 1], c='b')
    plt.show()






if __name__ == "__main__":
    main()