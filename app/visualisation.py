import matplotlib.pyplot as plt

def plot_data(data_stream, anomalies):
    
    # Plots the data stream and highlights detected anomalies.

    # Parameters:
    # - data_stream: List of numerical values representing the data stream.
    # - anomalies: List of indices representing the positions of anomalies in the data stream.
    
    # The function creates a line plot of the data stream and marks detected anomalies with red dots.

    # Plot the full data stream using a line plot
    plt.plot(data_stream, label="Data Stream")  # Line plot for the continuous data

    # Highlight anomalies in the data stream
    anomaly_indices = [i for i in range(len(data_stream)) if i in anomalies]  # Get indices of anomalies
    anomaly_values = [data_stream[i] for i in anomaly_indices]  # Get corresponding values for the anomalies

    # Plot anomalies on the same graph using red scatter points
    plt.scatter(anomaly_indices, anomaly_values, color='red', label="Anomalies")

    # Add a legend to indicate the data stream and anomalies
    plt.legend()

    # Set title and labels for the plot
    plt.title("Data Stream with Anomalies")
    plt.xlabel("Index")  # X-axis represents the index in the data stream
    plt.ylabel("Value")  # Y-axis represents the value of the data points

    # Display the plot to the user
    plt.show()
