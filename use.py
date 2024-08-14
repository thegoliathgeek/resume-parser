
import requests
import json
import google.generativeai as genai


API_KEY='******'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')



url = 'http://127.0.0.1:5000/process-pdf'
files = {'file': open('test-resume.pdf', 'rb')}
response = requests.post(url, files=files)
responseJson = response.json()
# print(responseJson['pdf_text'])

response = model.generate_content(f"{responseJson['pdf_text']}  \n ------ \n seggregate the data into different sections")
print(response.text)