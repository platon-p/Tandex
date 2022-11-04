e = [float(i) for i in input().split()]
e_predict = [float(i) for i in input().split()]

mse = sum([(i - j) ** 2 for i, j in zip(e, e_predict)]) / len(e)
mae = sum([abs(i - j) for i, j in zip(e, e_predict)]) / len(e)
rmse = mse ** 0.5


print(f'MSE: {mse:.2f}')
print(f'MAE: {mae:.2f}')
print(f'RMSE: {rmse:.2f}')
