import numpy as np
import matplotlib.pyplot as plt
import time

def quickSort(ar):
    if len(ar) == 1 or len(ar) == 0:
        return
    else:
        base = ar[0]
        left = 0
        right = len(ar) - 1

        while left != right:

            while ar[right] >= base and left != right:
                right -= 1
            ar[left] = ar[right]

            while ar[left] <= base and left != right:
                left += 1
            ar[right] = ar[left]

        ar[left] = base
        quickSort(ar[0:left])
        quickSort(ar[left+1: len(ar)])

#Swidge递增序列的希尔排序

def heerSort(ar):
    Sedgewick = [1, 5, 19, 41, 109, 209, 505, 929, 2161,
                   3905, 8929, 16001, 36289, 64769, 146305,
                   260609, 587521, 1045505, 2354689, 4188161,
                   9427969, 16764929, 37730305, 67884289,
                   150958081, 268386305, 603906049, 1073643521]
    i = 0
    keeper = 0
    while i < 28 :
        if Sedgewick[i] > len(ar):
            keeper = i - 1
            break
        i += 1


    while keeper >= 0:
        i = Sedgewick[keeper]
        j = i
        while j < len(ar):
            p = j
            temp = ar[p]

            while p > 0 and ar[p - i] > temp:
                ar[p] = ar[p - i]
                p -= i
            ar[p] = temp
            j += i
        keeper -= 1


size = 20000
A = np.random.random(size)
B = A.copy()

#heer
start = time.clock()
heerSort(A)
timeHeer = time.clock() - start

#quick
start = time.clock()
quickSort(B)
timeQuick = time.clock() - start

print("Time for heer is {}".format(timeHeer))
print("Time for quick is {}".format(timeQuick))


plt.plot(A)
plt.title("heer")
plt.show()

plt.plot(B)
plt.title("quick")
plt.show()

plt.plot(A - B)
plt.title("Heer - Quick")
plt.show()




