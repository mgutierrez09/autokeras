import os

from autokeras.utils import pickle_from_file
import numpy as np
import matplotlib.pyplot as plt


def load_searcher(path):
    return pickle_from_file(os.path.join(path, 'searcher'))


def get_data(path):
    searcher = load_searcher(path)

    indices = []
    times = []
    metric_values = []

    for index, item in enumerate(searcher.history):
        indices.append(index)
        metric_values.append(1 - item['metric_value'])
        times.append(item['time'])

    for i in range(1, len(times)):
        times[i] = times[i - 1] + times[i]
        metric_values[i] = min(metric_values[i], metric_values[i - 1])

    return indices, times, metric_values


def main(paths):
    indices = []
    times = []
    metric_values = []
    for path in paths:
        a, b, c = get_data(path)
        indices.append(a)
        times.append(b)
        metric_values.append(c)
    # evenly sampled time at 200ms intervals
    # t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    for i in range(len(paths)):
        plt.plot(indices[i], metric_values[i], 'r--')
    plt.show()

    print(times)
    for i in range(len(paths)):
        plt.plot(times[i], metric_values[i], 'b--')
    plt.show()


if __name__ == '__main__':
    main([''])