INPUT = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'setosa'}),
]

header = INPUT[0]
data = INPUT[1:]

for i, row in enumerate(data):
    spic = row[-1].pop()
    if spic.endswith("ca") or spic.endswith("sa"):
        print(spic)


INPUT = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

data = set()
for i, rows in enumerate(INPUT):
    for key in rows:
        data.add(key)

print(sorted(data))
