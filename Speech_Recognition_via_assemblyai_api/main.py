import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys

#Upload the local file to assebly ai
headers = {'authorization': API_KEY_ASSEMBLYAI}
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
filename =sys.argv[1]
def upload():
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data


    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))
    audio_url = upload_response.json()['upload_url']
    
    return audio_url




# Start the transcription process


def transcribe():
    trancript_request = { "audio_url": audio_url }

    transcript_response = requests.post(transcript_endpoint, json=trancript_request, headers=headers)
    
    job_id = trancript_request.json(['id'])
    return job_id

# keep polling the api till the transcription is done

#save the transcription to a file