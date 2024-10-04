def detect_anomalies(data_stream):
    # Detects anomalies in the data stream with error handling and data validation.
    if not data_stream:
        raise ValueError("Data stream cannot be empty.")
    
    if not all(isinstance(x, (int, float)) for x in data_stream):
        raise ValueError("All elements in the data stream must be numeric.")
    
    anomalies = []
    try:
        mean = sum(data_stream) / len(data_stream)
        std_dev = (sum((x - mean) ** 2 for x in data_stream) / len(data_stream)) ** 0.5

        for i, value in enumerate(data_stream):
            if abs(value - mean) > 3 * std_dev:
                anomalies.append(i)  # Store the index of the anomaly
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return anomalies




# Z-Score Based Detection
# This algorithm calculates the mean and standard deviation of the data stream. 
# Anomalies are detected as points that deviate more than 3 standard deviations from the mean.
# Effectiveness:
# It works well with normally distributed data, is computationally light, and is effective for real-time detection. 
# However, it struggles with non-normal distributions and may need recalibration if data patterns evolve over time.
