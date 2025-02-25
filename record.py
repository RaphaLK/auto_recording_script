import threading
from brainflow.board_shim import BoardShim, BrainFlowInputParams
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import pandas as pd

fs = 44100  
recording_time = 11

def record_emg():
  board.start_stream()
  print("EMG recording started!")

# Spk1_1001
def record_audio(speaker_number, trial_number):
  print("Audio recording started!")
  audio_data = sd.rec(int(fs * recording_time), samplerate=fs, device=7, channels=2)
  sd.wait()  # Wait until recording is finished
  write(f'Spk{speaker_number}_{trial_number}.wav', fs, audio_data)  # Save as WAV file
  print("Audio recording completed!")
  
def trim_recording(f_name, trial_number):
  emg_file = f"Spk{f_name}_{trial_number}.csv"
  emg_data = pd.read_csv(emg_file,delimiter=',')
  
# Initialize OpenBCI
BoardShim.enable_dev_board_logger()

params = BrainFlowInputParams()
params.serial_port = '/dev/ttyUSB0'  
board = BoardShim(0, params)  # 0 is the board ID for Cyton

print("Initializing OpenBCI Cyton...")
board.prepare_session()
f_name = input("Please input speaker number: ")
trial_number = input("Please input the trial number: ")

try:
  emg_thread = threading.Thread(target=record_emg)
  audio_thread = threading.Thread(target=record_audio, args=(f_name, trial_number))

  emg_thread.start()
  audio_thread.start()

  audio_thread.join()  # Wait for audio to finish

  data = board.get_board_data()
  board.stop_stream()
  board.release_session()

  np.savetxt(f"Spk{f_name}_{trial_number}.csv", data.transpose(), delimiter=',')
  print("Both recordings completed successfully!")

except Exception as e:
  print(f"Error: {e}")
  board.release_session()