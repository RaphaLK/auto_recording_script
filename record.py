import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams
import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # Sample rate
record_time = 12  # Seconds

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

myrecording = sd.rec(int(record_time * fs), samplerate=fs, channels=1) # mono
sd.wait()  # Wait until recording is finished

write(f'{f_name}.wav', fs, myrecording)  # Save as WAV file

# Stop EEG recording
board.stop_stream()
board.release_session()
print("Both recordings completed successfully!")
