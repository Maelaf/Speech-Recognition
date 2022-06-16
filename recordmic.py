#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio
import wave


# In[2]:


FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000


# In[3]:


p = pyaudio.PyAudio()


# In[4]:


stream = p.open( 
        format = FORMAT,
        channels = CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER)

print("start recordint")

seconds = 5


# In[6]:


frames=[]

for i in range( 0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
    
stream.stop_stream()
stream.close()
p.terminate()


# In[ ]:


obj = wave.open("out.wav","wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()

