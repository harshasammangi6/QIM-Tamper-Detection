from qim_embed import embed_watermark
from qim_detect import detect_tampering
import numpy as np
import time

def simulate_stream():
    original = np.random.randint(0, 256, 100)
    watermark = np.random.randint(0, 2, 100)
    embedded = embed_watermark(original, watermark)
    
    # Simulate tampering in stream
    received = embedded.copy()
    received[20] += 10

    tampered_indices = detect_tampering(embedded, received)
    print("Stream processed. Tampering at:", tampered_indices)

if __name__ == "__main__":
    print("Starting simulated stream...")
    time.sleep(1)
    simulate_stream()
