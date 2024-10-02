from data_stream import generate_data_stream
from detection import detect_anomalies
from visualisation import plot_data

def main():
    """Main function to execute the anomaly detection process."""
    data_stream = generate_data_stream(100)
    detected_anomalies = detect_anomalies(data_stream)
    plot_data(data_stream, detected_anomalies)

if __name__ == "__main__":
    main()
