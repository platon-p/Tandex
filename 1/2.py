e = [float(i) for i in input().split()]
e_predict = [float(i) for i in input().split()]

e_avg = sum(e) / len(e)

r2 = 1 - (sum([(i - j) ** 2 for i, j in zip(e, e_predict)]) / sum([(e_avg - i) ** 2 for i in e]))
print(f'R2: {r2:.2f}')
