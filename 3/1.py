import numpy as np


def onehot_encoding(x):
    u = np.unique(x)
    y = np.zeros([x.shape[0], u.shape[0]], int)
    for i in range(len(x)):
        y[i][np.where(u == x[i])[0][0]] = 1
    return y


print(onehot_encoding(np.array(['1', '2'])))