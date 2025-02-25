from brainflow.board_shim import BoardShim, BrainFlowInputParams
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pandas as pd
import librosa

def trim_recording(f_name, trial_number):
  emg_file = f"Spk{f_name}_{trial_number}.csv"
  audio_file = f"Spk{f_name}_{trial_number}.wav"
  emg_data = pd.read_csv(emg_file,delimiter=',')
  audio_data,sr = librosa.load(audio_file, mono=True)
  emg_duration = emg_data.shape[0] / 250
  
  # Trim audio to match EMG duration
  target_samples = int(emg_duration * sr)
  audio_data_trimmed = audio_data[:target_samples]
  
  write(f'Spk{f_name}_{trial_number}.wav', sr, audio_data_trimmed)  


fs = 44100  # Sample rate
recording_time = 15
# Initialize OpenBCI
BoardShim.enable_dev_board_logger()


params = BrainFlowInputParams()

params.serial_port = '/dev/ttyUSB0'  
board = BoardShim(0, params)  # 0 is the board ID for Cyton

print("Initializing OpenBCI Cyton...")
board.prepare_session()
f_name = input("Please input Speaker ID: ")
trial_number = input("Please input trial no.: ")


# Start EEG recording
board.start_stream()
print("Recording...")

# Set Device and Channel accordingly
myrecording = sd.rec(int(fs * recording_time), samplerate=fs, device=7,channels=1)

# Stop EMG recording
while(1):
  stop = input()
  if (stop == " "):
    break
  continue
  
sd.stop()
write(f'Spk{f_name}_{trial_number}.wav', fs, myrecording)  # Save as WAV file
data = board.get_board_data()
board.stop_stream()
board.release_session()
np.savetxt(f"Spk{f_name}_{trial_number}.csv", data.transpose(), delimiter=',')
trim_recording(f_name, trial_number)
print("Both recordings completed successfully!")

