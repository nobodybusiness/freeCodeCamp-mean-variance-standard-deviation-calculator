import numpy as np


def calculate(list) -> dict:
    """
    Uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    """
    # The input of the function should be a list containing 9 digits.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape((3, 3))

    calculations: dict = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": [],
    }
    # mean
    calculations["mean"].append(arr.mean(axis=0).tolist())
    calculations["mean"].append(arr.mean(axis=1).tolist())
    calculations["mean"].append(arr.flatten().mean().tolist())
    # variance
    calculations["variance"].append(arr.var(axis=0).tolist())
    calculations["variance"].append(arr.var(axis=1).tolist())
    calculations["variance"].append(arr.flatten().var().tolist())
    # standard deviation
    calculations["standard deviation"].append(arr.std(axis=0).tolist())
    calculations["standard deviation"].append(arr.std(axis=1).tolist())
    calculations["standard deviation"].append(arr.flatten().std().tolist())
    # max
    calculations["max"].append(arr.max(axis=0).tolist())
    calculations["max"].append(arr.max(axis=1).tolist())
    calculations["max"].append(arr.flatten().max().tolist())
    # min
    calculations["min"].append(arr.min(axis=0).tolist())
    calculations["min"].append(arr.min(axis=1).tolist())
    calculations["min"].append(arr.flatten().min().tolist())
    # sum
    calculations["sum"].append(arr.sum(axis=0).tolist())
    calculations["sum"].append(arr.sum(axis=1).tolist())
    calculations["sum"].append(arr.flatten().sum().tolist())

    return calculations
