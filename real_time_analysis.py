from scipy.signal import find_peaks

def detect_anomalies(signal, threshold=0.5):
    peaks, _ = find_peaks(signal, height=threshold)
    return peaks
