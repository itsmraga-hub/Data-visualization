import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues,
            edgecolor='none', s=10)

plt.axis([0, 1100, 0, 1100000000])

plt.show()
