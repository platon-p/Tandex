import pandas as pd
import numpy as np

df = pd.read_csv('penguins.csv')
df = df.dropna()
a = df.loc[:, ['bill_length_mm', 'bill_depth_mm']].to_numpy()
n, k = int(input()), int(input())
sums = np.sum(np.square(a - a[n]), axis=1)
print(*a[sums.argsort()][1:k + 1], sep='\n')