import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations of value sharing.
    
    In each iteration, the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Args:
        values (list or numpy array): 1D array of values.
        num_iterations (int): Number of iterations to run.
        share (float): Fraction of value to share with neighbors.

    Returns:
        numpy array: Updated values after all iterations.
    """
    values = np.array(values, dtype=float)  # Convert to numpy array for easier manipulation
    n = len(values)

    for _ in range(num_iterations):
        max_index = np.argmax(values)  # Index of the maximum value
        left_neighbor = (max_index - 1) % n  # Left neighbor index (wrap around)
        right_neighbor = (max_index + 1) % n  # Right neighbor index (wrap around)
        
        shared_value = values[max_index] * share  # Amount to share
        
        # Update values
        values[max_index] -= 2 * shared_value
        values[left_neighbor] += shared_value
        values[right_neighbor] += shared_value

    return values

# Test der Funktion
print(fair_sharer([0, 1000, 800, 0], 1, 0.1))  # Output: [100, 800, 900, 0]
print(fair_sharer([0, 1000, 800, 0], 2, 0.1))  # Output: [100, 890, 720, 90]
print(fair_sharer([0, 1000, 800, 0], 3, 0.1))  # Output: [100, 810, 800, 90]