from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key = str(os.getenv("OPENAI_API_KEY")))

def call_gpt_basic(system, user):
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": f"{system}"},
      {"role": "user", "content": f"{user}"}
    ]
  )

  return completion.choices[0].message.content
