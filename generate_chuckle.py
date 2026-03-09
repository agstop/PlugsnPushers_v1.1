import wave
import struct
import math
import random

SAMPLE_RATE = 44100
DURATION = 2.0

def generate_chuckle(filename):
    print("Generating sleazy chuckle...")
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        
        for i in range(int(SAMPLE_RATE * DURATION)):
            t = i / SAMPLE_RATE
            
            # Base ha-ha-ha pattern (rhythmic pulsing around 4-6 Hz)
            pulse = (math.sin(t * 5.0 * 2 * math.pi) + 1.0) / 2.0
            
            # Raspy throat vibration (low frequency square/sawtooth mix)
            throat = math.sin(t * 85.0 * 2 * math.pi) + 0.5 * math.sin(t * 170.0 * 2 * math.pi)
            
            # Breath/noise for the "hhh" sound
            noise = random.uniform(-1, 1) * 0.4
            
            # Envelope to fade in and out gracefully over the 2 seconds
            envelope = 1.0
            if t < 0.1:
                envelope = t / 0.1
            elif t > 1.8:
                envelope = max(0.0, (2.0 - t) / 0.2)
                
            # Combine the elements into a raspy, rhythmic laughing breath
            sample = (throat * 0.6 + noise) * pulse * envelope * 0.8
            
            # Clip
            sample = max(-1.0, min(1.0, sample))
            
            value = int(sample * 32767)
            wav_file.writeframes(struct.pack('<h', value))
            
    print("Done generated:", filename)

if __name__ == "__main__":
    generate_chuckle("app/src/main/res/raw/chuckle.wav")
