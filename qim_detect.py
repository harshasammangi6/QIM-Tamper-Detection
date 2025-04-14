import numpy as np

def detect_tampering(original, received, delta=1):
    tampered_indices = []
    for i in range(len(original)):
        if abs(original[i] - received[i]) > delta:
            tampered_indices.append(i)
    return tampered_indices

if __name__ == "__main__":
    original = np.random.randint(0, 256, 100)
    received = original.copy()
    received[10] += 5  # simulate tampering
    tampered = detect_tampering(original, received)
    print("Tampering detected at indices:", tampered)
