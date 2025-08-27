import numpy as np


def calculate_bin_statistics(x, y, bin_edges):
    
    """ 
    This function calculates the median and standard deviation of y values 
    within each bin defined by the bin edges.

    Inputs:
      x: A NumPy array of x data.
      y: A NumPy array of y data (same length as x).
      bin_edges: A list or NumPy array of bin edges for x data.

    Output:
      A tuple containing three elements:
          - x_medians: A NumPy array containing the median of x values in each bin.
          - y_medians: A NumPy array containing the median of y values in each bin.
          - y_errors: A NumPy array containing the standard deviation of y values in each bin.
    """
      
   

    n_bins = len(bin_edges) - 1

    x_medians = np.zeros(shape=n_bins)
    y_medians = np.zeros(shape=n_bins)
    y_errors = np.zeros(shape=n_bins)

    for i in range(n_bins):
        xmask = np.logical_and(x > bin_edges[i], x < bin_edges[i + 1])
        
        x_medians[i] = np.median(x[xmask])

        y_medians[i] = np.median(y[xmask])
        
        y_errors[i] = np.std(y[xmask])

    return x_medians, y_medians, y_errors



def sort_by_frequency(arr):
    """
    Sorts array based on the frequency of unique values
    arr: numpy array 
    
    Returns:
    numpy array sorted based on frequency of array elements
    
    """
    
    # Get unique values and their counts
    unique, counts = np.unique(arr, return_counts=True)
    
    # Sort unique values by their counts
    sorted_indices = np.argsort(counts)
    sorted_unique = unique[sorted_indices]
    
    # Create a mapping from value to its sorted index based on frequency
    value_to_sorted_index = {val: idx for idx, val in enumerate(sorted_unique)}
    
    # Sort the original array by the sorted indices
    sorted_arr = sorted(arr, key=lambda x: value_to_sorted_index[x])
    
    return np.array(sorted_arr)
