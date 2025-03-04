import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import librosa
f_name = input("Please input Speaker ID: ")
trial_number = input("Please input trial no.: ")

emg_data = np.read_csv(f"Spk{f_name}_{trial_number}.csv",delimiter=',')
audio_data,sr = librosa.read(f'Spk{f_name}_{trial_number}.wav')

emg_time = np.linspace(0,emg_data.shape[0]/250,emg_data.shape[0])
audio_time = np.linspace(0,len(audio_data) / sr, len(audio_data))
ch1 = emg_data.iloc[0:,0]
ch2 = emg_data.iloc[0:,1]
ch3 = emg_data.iloc[0:,2]
ch4 = emg_data.iloc[0:,3]
# Plot the data
figure, axis = plt.subplots(5, 1, figsize=(25, 12))
plt.subplots_adjust(hspace=5)

axis[0].plot(time_audio, audio_data, label="Audio")
axis[0].set_xlabel("Time (s)")
axis[0].set_ylabel("Amplitude")
axis[0].set_title(prompt)
axis[0].grid(True)


axis[1].plot(time_emg, ch1)
axis[1].set_xlabel("Time (s)")
axis[1].set_ylabel("Amplitude")
axis[1].set_title("EMG Data Channel 0")
# axis[1].grid(True)

axis[2].plot(time_emg, ch2)
axis[2].set_xlabel("Time (s)")
axis[2].set_ylabel("Amplitude")
axis[2].set_title("EMG Data Channel 1")
axis[2].grid(True)

axis[3].plot(time_emg, ch3)
axis[3].set_xlabel("Time (s)")
axis[3].set_ylabel("Amplitude")
axis[3].set_title("EMG Data Channel 2")
axis[3].grid(True)

axis[4].plot(time_emg, ch4)
axis[4].set_xlabel("Time (s)")
axis[4].set_ylabel("Amplitude")
axis[4].set_title("EMG Data Channel 3")
axis[4].grid(True)

plt.tight_layout()
plt.show()