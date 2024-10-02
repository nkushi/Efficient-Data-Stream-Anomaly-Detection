import matplotlib.pyplot as plt

def plot_data(data_stream, anomalies):
    """Plots the data stream and highlights detected anomalies."""
    plt.plot(data_stream, label="Data Stream")
    
    # Highlight anomalies
    anomaly_indices = [i for i in range(len(data_stream)) if i in anomalies]
    anomaly_values = [data_stream[i] for i in anomaly_indices]
    
    plt.scatter(anomaly_indices, anomaly_values, color='red', label="Anomalies")
    plt.legend()
    plt.title("Data Stream with Anomalies")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()
