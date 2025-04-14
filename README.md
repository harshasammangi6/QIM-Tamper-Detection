# QIM-Tamper-Detection
A research implementation of QIM-based watermarking for tamper detection in live streaming media
# QIM-Based Tamper Detection for Live Streaming Media

This repository contains the implementation of **Quantization Index Modulation (QIM)** watermarking for **real-time tamper detection** in live streaming content. This project is part of my Ph.D. research at Dakota State University.

## 🧠 About the Project

Live streaming media is increasingly vulnerable to unauthorized modifications and content tampering. To address this, we present a QIM-based watermarking technique designed to:

- Embed imperceptible watermarks in streaming data
- Detect any modifications or tampering
- Support real-time detection without affecting stream latency

## 🧪 Features

- ✅ Watermark embedding using QIM
- ✅ Tamper detection via watermark extraction
- ✅ Lightweight implementation (Python)
- ✅ Real-time stream simulation
- ✅ Visualization of tampered vs. original frames

## 🛠️ Project Structure

```plaintext
QIM-Tamper-Detection/
│
├── qim_embed.py        # Embeds watermark into media stream
├── qim_detect.py       # Extracts watermark and detects tampering
├── demo_stream.py      # Simulated stream environment
├── watermark_utils.py  # Core functions for QIM processing
├── sample_frames/      # Example input media
└── README.md           # This file
