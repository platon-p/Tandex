import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('penguins.csv')
df = df.dropna()

labels = df['species']
features = df.loc[:, ['bill_length_mm', 'bill_depth_mm']]

train_features, test_features, train_labels, test_labels = \
    train_test_split(features, labels, test_size=0.2, random_state=123)

accuracies = {}
for i in range(1, 11):
    alg_u = KNeighborsClassifier(n_neighbors=i, weights='uniform')
    alg_u.fit(train_features, train_labels)

    alg_d = KNeighborsClassifier(n_neighbors=i, weights='distance')
    alg_d.fit(train_features, train_labels)

    accuracies[i] = [alg_u.score(test_features, test_labels), alg_d.score(test_features, test_labels)]

best_accuracy = max([max(i) for i in accuracies.values()])
worst_accuracy = min([min(i) for i in accuracies.values()])

print(f'Best accuracy: {best_accuracy:.6f}')
print(f'Worst accuracy: {worst_accuracy:.6f}')