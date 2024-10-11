import numpy as np

def main():
    signal = []
    for data in read_signal():
        signal.append(data)
        if len(signal) > 1000:  # Process every 1000 samples
            filtered_signal = bandpass_filter(signal, 0.5, 50.0, 1000)
            anomalies = detect_anomalies(filtered_signal)
            if anomalies:
                alert_user("Anomaly detected!")
                plot_signal(filtered_signal, anomalies)
            signal = []  # Reset signal buffer

if __name__ == "__main__":
    main()
