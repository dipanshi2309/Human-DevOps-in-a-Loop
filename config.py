import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-2.5-flash")