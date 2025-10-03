#!/usr/bin/env python3
# 528hz_one_hour.py
import numpy as np
from scipy.io.wavfile import write

# ------------------ Parameters ------------------
freq_hz   = 528          # Desired frequency
duration  = 3600         # seconds (1 hour)
sample_rate = 44100      # CD quality, Hz
amplitude  = 0.5         # 0.0 to 1.0 (avoids clipping)

# ------------------ Generate -------------------
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
wave = amplitude * np.sin(2 * np.pi * freq_hz * t)

# Make it stereo: duplicate the mono channel
stereo_wave = np.column_stack((wave, wave))

# Convert to 16‑bit PCM (range -32767 … 32767)
stereo_wave_int = np.int16(stereo_wave * 32767)

# ------------------ Write to disk -------------------
output_file = "c:\\projects\\sound generator\\528Hz_one_hour.wav"
write(output_file, sample_rate, stereo_wave_int)

print(f"✅  {output_file} generated ({stereo_wave_int.nbytes / (1024*1024):.1f} MiB)")
