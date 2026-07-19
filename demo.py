from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client=Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com"
)
audio_file=open(r"C:\Users\Lohith\Videos\tel_story_1970_01.mp3",'rb')
output=client.audio.transcriptions.create(
      file=audio_file, # Required audio file
      model="whisper-large-v3-turbo",
      language="te"
) 
print(output.text)     