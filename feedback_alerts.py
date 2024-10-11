import matplotlib.pyplot as plt

def plot_signal(signal, peaks):
    plt.plot(signal)
    plt.plot(peaks, signal[peaks], "x")
    plt.show()

def alert_user(message):
    print(f"Alert: {message}")

# Example usage
signal = list(read_signal())
filtered_signal = bandpass_filter(signal, 0.5, 50.0, 1000)
anomalies = detect_anomalies(filtered_signal)

if anomalies:
    alert_user("Anomaly detected!")
    plot_signal(filtered_signal, anomalies)
