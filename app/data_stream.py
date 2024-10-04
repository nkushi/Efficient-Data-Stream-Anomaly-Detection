import random

def generate_data_stream(num_points=100):
    # Generates a simulated data stream with anomalies.
    data_stream = []
    for _ in range(num_points):
        # Simulate normal values
        value = random.uniform(-0.05, 0.05)
        # Randomly introduce anomalies
        if random.random() < 0.1:  # 10% chance to create an anomaly
            value *= 10  # Increase the value to simulate an anomaly
        data_stream.append(value)
    return data_stream
