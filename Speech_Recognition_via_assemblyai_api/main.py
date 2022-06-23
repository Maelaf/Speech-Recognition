import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys

#Upload the local file to assebly ai
headers = {'authorization': API_KEY_ASSEMBLYAI}
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
filename =sys.argv[0]
def upload(filename):
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


def transcribe(audio_url):
    transcript_request = { "audio_url": audio_url }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    
    job_id = transcript_response.json()['id']
    return job_id


audio_url= upload(filename)
transcript_id= transcribe(audio_url)



# keep polling the api till the transcription is done
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url():
    transcript_id = transcribe()

    while True:
        data = poll(transcirpt_id)
        polling_response = requests.get(polling_endpoint, headers=headers)
        if data['status'] == 'completed':

            return polling_response
        elif data['status'] == 'error':
            return "error"


#save the transcription to a file