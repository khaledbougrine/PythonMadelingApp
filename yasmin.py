import numpy as np


def find_Max(Tab, n):
    mi = 1
    max = Tab[0]
    for i in range(1, n-1):
        if Tab[i] > max:
            max = Tab[i]
            mi = i
    a = Tab[n-1]
    Tab[n-1] = max
    Tab[mi] = a
    return Tab


if __name__ == '__main__':
    tab = [1000, 90000, 8, 1,999,10]
    n = 6
    Tab =find_Max(tab, n)
    print(Tab)
