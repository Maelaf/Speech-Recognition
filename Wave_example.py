# Audio file formats
# mp3 - are lossy compression format, most common type.
# flac - lossless compression, allows perfect reconstruction
# wav - are uncompressed format, best audio quality but takes up large size. standard cd format

import wave

# Audio signal parameters
# - number of channels
# - sample width - number of bytes for each sample
# - framerate - number of samples per second, 44,100 Hz
# - nframes - number of frames in the audio file
# - values of a frame - the actual audio data
obj = wave.open('output.wav', 'rb')

print('Number of channels: ', obj.getnchannels())
print('Sample width: ', obj.getsampwidth())
print('Frame rate: ', obj.getframerate())
print('Number of frames: ', obj.getnframes())
print(' Parameters: ', obj.getparams() )

t_audio = obj.getnframes() / obj.getframerate()
print('Audio duration: ', t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj_new = wave.open("output_new.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()