from sanitize_json import sanitize_json
from schema import example
from extract_texts_from_PDF import extract_text
from openai import OpenAI
import json

client = OpenAI()

text = extract_text('./Karte_Salon_Pitzelberger.pdf')
prompt_1 = f"""Please convert the menu categories and menu items which belong to the category from the provided text into the specific schema:
{text} \n
Schema:
{example}
"""

print(text)
# print(prompt_1)

response_1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.3,
    messages=[
    {"role": "system", "content": "You are a helpful assistant that converts categories and items from the provided text into the specific schema"},
    {"role": "user", "content": prompt_1},
    ],
)

json_data = response_1.choices[0].message.content

# Export in json file
file_path = "converted_menu.json"
with open(file_path, "w", encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=2, ensure_ascii=False)

# When reading the JSON file, you can also specify the encoding
with open(file_path, 'r', encoding='utf-8') as json_file:
   loaded_data = json.load(json_file)

print(loaded_data)