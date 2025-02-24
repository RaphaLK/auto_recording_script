import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

fs = 44100  # Sample rate
recording_time = 10
# Initialize OpenBCI
BoardShim.enable_dev_board_logger()


params = BrainFlowInputParams()

params.serial_port = '/dev/ttyUSB0'  
board = BoardShim(0, params)  # 0 is the board ID for Cyton

print("Initializing OpenBCI Cyton...")
board.prepare_session()
f_name = input("Please input the name of the recording  ")


# Start EEG recording
board.start_stream()
print("EEG recording started!")
print("Recording...")

# Set Device and Channel accordingly
myrecording = sd.rec(int(fs * recording_time), samplerate=fs, device=7,channels=2)


# Stop EMG recording
while(1):
  stop = input()
  if (stop == " "):
    break
  continue
  
sd.stop()
write(f'{f_name}.wav', fs, myrecording)  # Save as WAV file
data = board.get_board_data()
board.stop_stream()
board.release_session()
np.savetxt(f"{f_name}.csv", data.transpose(), delimiter=',')
print(f"Data saved as {f_name}")
print("Both recordings completed successfully!")

