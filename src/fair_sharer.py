import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    values = np.array(values, dtype=float)
    n = len(values)

    for _ in range(num_iterations):
        max_index = np.argmax(values)
        left_neighbor = (max_index - 1) % n
        right_neighbor = (max_index + 1) % n
        
        shared_value = values[max_index] * share

        values[max_index] -= 2 * shared_value
        values[left_neighbor] += shared_value
        values[right_neighbor] += shared_value

    return values

if __name__ == "__main__":
    print(fair_sharer([0, 1000, 800, 0], 1, 0.1))
    print(fair_sharer([0, 1000, 800, 0], 2, 0.1))
    print(fair_sharer([0, 1000, 800, 0], 3, 0.1))