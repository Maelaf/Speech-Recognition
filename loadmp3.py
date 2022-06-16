#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")


#increse the volube by 6dB
audio = audio + 6
#repeat
audio = audio *2
#fade in 2 sec
audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")

print("done")

