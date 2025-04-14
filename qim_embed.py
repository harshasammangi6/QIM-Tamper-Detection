import numpy as np

def embed_watermark(data, watermark, delta=1):
    watermarked_data = data.copy()
    for i in range(len(watermark)):
        bit = watermark[i]
        if bit == 1:
            watermarked_data[i] = (data[i] // (2 * delta)) * (2 * delta) + delta
        else:
            watermarked_data[i] = (data[i] // (2 * delta)) * (2 * delta)
    return watermarked_data

if __name__ == "__main__":
    data = np.random.randint(0, 256, 100)
    watermark = np.random.randint(0, 2, 100)
    embedded = embed_watermark(data, watermark)
    print("Watermark embedded successfully.")
