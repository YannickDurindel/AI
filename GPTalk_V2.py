import sounddevice as sd
import soundfile as sf
import numpy as np
import pydub

# Set the audio parameters
SAMPLE_RATE = 44100
RECORD_SECONDS = 5  # Adjust the recording duration as needed
OUTPUT_FILE = "output.mp3"  # Specify the output file name

# Start the audio recording
print("Recording started. Speak into the microphone...")
recording = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
sd.wait()  # Wait for the recording to complete

print("Recording completed.")

# Convert the recorded audio to the desired format (MP3)
audio_data = np.squeeze(recording)
sf.write("output.wav", audio_data, samplerate=SAMPLE_RATE)  # Save as WAV file

# Load the WAV file and convert it to MP3
wav_data, _ = sf.read("output.wav")
audio_segment = pydub.AudioSegment.from_wav("output.wav")
audio_segment.export(OUTPUT_FILE, format="mp3")  # Export as MP3

print(f"Audio saved as {OUTPUT_FILE}")
