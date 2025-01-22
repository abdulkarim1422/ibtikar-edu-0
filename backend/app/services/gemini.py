import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=str(os.getenv("GOOGLE_API_KEY")))

def call_gemini_basic(x):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(x)
    return response.text



if __name__ == "__main__":
    print(call_gemini_basic("write a summary of this article: https://arxiv.org/abs/2308.10383"))
