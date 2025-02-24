import sounddevice as sd

devices = sd.query_devices()

for device_index, device in enumerate(devices):
    print(f"Device {device_index}: {device['name']}")
    if 'max_input_channels' in device and device['max_input_channels'] > 0:
        print(f"  Max input channels: {device['max_input_channels']}")
        print(f"  Supported Sample Rates: {device['default_samplerate']}")
    else:
        print("  No input channels or device is not an input device.")