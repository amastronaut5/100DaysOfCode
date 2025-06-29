#PDF TO AUDIOBOOK
from murf import Murf
import requests
from PyPDF2 import PdfReader, PageObject


#TAKING USER INPUT
file = input("Enter the file address: ")

#READ FROM PDF
def readFrompdf():

    reader = PdfReader(f"{file}")
    no_pages = len(reader.pages)
    page=PageObject()
    text=""
    for i in range(no_pages):
        page=reader.pages[i]
        text += page.extract_text()

    return text[0:3000]

# print(text)

#TEXT TO AUDIO
MURF_API_KEY = "ap2_01dd5194-0cbd-4668-adfb-d1611009cc3e"
client = Murf(api_key=MURF_API_KEY)

response = client.text_to_speech.generate(
    text=readFrompdf(),
    voice_id="en-US-natalie"
)

print(response.audio_file)

# CAMB_API_KEY="be23b50c-b38a-4788-a67f-bf1f9ff03a06"
# url = "https://client.camb.ai/apis/list-voices"
# headers={"x-api-key":CAMB_API_KEY}
# response = requests.get(url, headers=headers)
# data = response.json()