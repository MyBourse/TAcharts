import numpy as np

from .wrappers import pd_series_to_np_array


@pd_series_to_np_array
def crossover(x1, x2):
    ''' Find all instances of intersections between two lines '''

    x1_gt_x2 = x1 > x2
    cross = np.diff(x1_gt_x2)
    cross = np.insert(cross, 0, False)
    cross_indices = np.flatnonzero(cross)
    return cross_indices
