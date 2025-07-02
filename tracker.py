import os
from google import genai
from google.genai import types

my_api_key = os.getenv('GENAI_KEY')
genai.api_key = my_api_key

client = genai.Client(
    api_key=my_api_key,
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
      system_instruction="You are acting as a financial advisor, give good financial decisions and reccomendations for a person"
    ),
    contents="Based off the following datatable of expenses, provide reccomendations to this person for budgeting and their expenses",
)

print(response.text)
