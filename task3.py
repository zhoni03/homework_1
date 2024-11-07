import numpy as np

def time_to_cyclic(hour):
    """
    Converts an hour (0-24) to cyclic sine and cosine features for a 24-hour cycle.
    """
    radians = (hour % 24) * (2 * np.pi / 24)
    return np.sin(radians), np.cos(radians)

def cyclic_time_difference(hour1, hour2):
    """
    Computes the difference between two hours in a cyclic 24-hour format.
    """
    sin1, cos1 = time_to_cyclic(hour1)
    sin2, cos2 = time_to_cyclic(hour2)
    
    # Calculate Euclidean distance to find effective cyclic difference
    return np.arccos(sin1 * sin2 + cos1 * cos2) * (24 / (2 * np.pi))

# Example usage:
print(time_to_cyclic(23))  # Convert 23:00 to cyclic representation
print(time_to_cyclic(1))   # Convert 01:00 to cyclic representation
print(cyclic_time_difference(23, 1))  # Should output around 2 hours
