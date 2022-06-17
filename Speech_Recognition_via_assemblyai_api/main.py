import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys

#Upload the local file to assebly ai

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
filename =sys.argv[1]

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))

print(response.json())


# Start the transcription process

audio_url = response.json()['upload_url']

json = { "audio_url": audio_url }

response = requests.post(transcript_endpoint, json=json, headers=headers)
print(response.json()

# keep pulling the api till the transcription is done

#save the transcription to a file