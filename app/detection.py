def detect_anomalies(data_stream):
    """Detects anomalies in the data stream based on a simple statistical method."""
    anomalies = []
    mean = sum(data_stream) / len(data_stream)
    std_dev = (sum((x - mean) ** 2 for x in data_stream) / len(data_stream)) ** 0.5
    
    for i, value in enumerate(data_stream):
        # Assuming an anomaly is defined as a value outside 3 standard deviations
        if abs(value - mean) > 3 * std_dev:
            anomalies.append(i)  # Store the index of the anomaly
    return anomalies
