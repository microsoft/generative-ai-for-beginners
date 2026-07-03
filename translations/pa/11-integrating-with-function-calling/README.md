# ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ

[![ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ](../../../translated_images/pa/11-lesson-banner.d78860d3e1f041e2.webp)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

ਤੁਸੀਂ ਪਹਿਲਾਂ ਦੇ ਪਾਠਾਂ ਵਿੱਚ ਕਾਫੀ ਕੁਝ ਸਿੱਖਿਆ ਹੈ। ਹਾਲਾਂਕਿ, ਅਸੀਂ ਹੋਰ ਸੁਧਾਰ ਕਰ ਸਕਦੇ ਹਾਂ। ਕੁਝ ਚੀਜ਼ਾਂ ਜੋ ਅਸੀਂ ਦਰੁਸਤ ਕਰ ਸਕਦੇ ਹਾਂ ਉਹ ਇਹ ਹਨ ਕਿ ਅਸੀਂ ਇੱਕ ਵਧੇਰੇ ਲਗਾਤਾਰ ਜਵਾਬ ਫਾਰਮੈਟ ਕਿਵੇਂ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ ਤਾਂ ਜੋ ਜਵਾਬ ਦੇ ਨਾਲ ਕੰਮ ਕਰਨਾ ਆਸਾਧਾ ਹੋ ਜਾਵੇ। ਨਾਲ ਹੀ, ਅਸੀਂ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਹੋਰ ਸਮਪੰਨ ਬਣਾਉਣ ਲਈ ਹੋਰ ਸਰੋਤਾਂ ਤੋਂ ਡੇਟਾ ਸ਼ਾਮਿਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਸਕਦੇ ਹਾਂ।

ਉਪਰੋਕਤ ਸਮੱਸਿਆਵਾਂ ਨੁੰ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਹੱਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ।

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ:

- ਸਮਝਾਓ ਕਿ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਕੀ ਹੈ ਅਤੇ ਇਸ ਦੇ ਪ੍ਰਯੋਗ ਕੇਸ ਕੀ ਹਨ।
- Azure OpenAI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉਣਾ।
- ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਫੰਕਸ਼ਨ ਕਾਲ ਕਿਵੇਂ ਇੰਟੀਗ੍ਰੇਟ ਕਰੀਏ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਦੇ ਉਦੇਸ਼ ਨੂੰ ਸਮਝਾਉਣਾ।
- Azure OpenAI ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫੰਕਸ਼ਨ ਕਾਲ ਸੈਟਅਪ ਕਰਨਾ।
- ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਕੇਸ ਲਈ ਪ੍ਰਭਾਵਸ਼ালী ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਡਿਜ਼ਾਈਨ ਕਰਨਾ।

## ਸੰਦਰਭ: ਫੰਕਸ਼ਨਾਂ ਨਾਲ ਸਾਡਾ ਚੈਟਬੋਟ ਸੁਧਾਰਨਾ

ਇਸ ਪਾਠ ਲਈ, ਅਸੀਂ ਆਪਣੇ ਸਿੱਖਿਆ ਸਟਾਰਟਅੱਪ ਲਈ ਇੱਕ ਫੀਚਰ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ ਚੈਟਬੋਟ ਵਰਤ ਕੇ ਤਕਨੀਕੀ ਕੋਰਸਾਂ ਲੱਭਣ ਦੀ ਆਗਿਆ ਦੇਵੇ। ਅਸੀਂ ਉਹ ਕੋਰਸ ਸਿਫਾਰਿਸ਼ ਕਰਾਂਗੇ ਜੋ ਉਨ੍ਹਾਂ ਦੀ ਹੁਨਰ ਦੇ ਪੱਧਰ, ਮੌਜੂਦਾ ਭੂਮਿਕਾ ਅਤੇ ਰੁਚੀ ਵਾਲੀ ਤਕਨਾਲੋਜੀ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹੋਣ।

ਇਸ ਸੰਦਰਭ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਅਸੀਂ ਇਸਨਾਂ ਦੀ ਮਿਲੀ-ਜੁਲੀ ਵਰਤੋਂ ਕਰਾਂਗੇ:

- `Azure OpenAI` ਯੂਜ਼ਰ ਲਈ ਚੈਟ ਅਨੁਭਵ ਬਣਾਉਣ ਲਈ।
- `Microsoft Learn Catalog API` ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ ਉਨ੍ਹਾਂ ਦੀ ਬੇਨਤੀ ਦੇ ਆਧਾਰ 'ਤੇ ਕੋਰਸ ਲੱਭਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।
- `Function Calling` ਜੋ ਯੂਜ਼ਰ ਦੀ ਪੁੱਛਤाछ ਲੈ ਕੇ ਉਸਨੂੰ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਭੇਜਦਾ ਹੈ ਤਾਂ ਜੋ API ਬੇਨਤੀ ਕੀਤੀ ਜਾ ਸਕੇ।

ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਪਹਿਲਾਂ ਕਿਉਂ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਾਂ:

## ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਕਿਉਂ

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਤੋਂ ਪਹਿਲਾਂ, LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਅਸੰਗਠਿਤ ਅਤੇ ਇਨਕਨਸਿਸਟੈਂਟ ਹੁੰਦੇ ਸਨ। ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਹਰ ਜਵਾਬ ਦੀ ਵੱਖ-ਵੱਖ ਕਿਸਮ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਜਟਿਲ ਵੈਧਤਾ ਕੋਡ ਲਿਖਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਸੀ। ਯੂਜ਼ਰ "ਸਟਾਕਹੋਲਮ ਦਾ ਮੌਜੂਦਾ ਮੌਸਮ ਕੀ ਹੈ?" ਵਰਗੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਨਹੀਂ ਲੈ ਸਕਦੇ ਸਨ। ਇਹ ਇਸ ਲਈ ਸੀ ਕਿ ਮਾਡਲਾਂ ਦੀ ਸਿੱਖਿਆ ਤਿਆਰ ਕੀਤੀ ਗਈ ਡੇਟਾ ਦੇ ਸਮੇਂ ਤੱਕ ਸੀਮਿਤ ਸੀ।

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ Azure OpenAI ਸੇਵਾ ਦੀ ਇੱਕ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਜੋ ਹੇਠ ਲਿਖੀਆਂ ਸੀਮਾਵਾਂ ਨੂੰ ਮਾਤ ਹੁੰਦੀ ਹੈ:

- **ਲਗਾਤਾਰ ਜਵਾਬ ਫਾਰਮੈਟ**। ਜੇ ਅਸੀਂ ਜਵਾਬ ਫਾਰਮੈਟ ਤੇ ਬਿਹਤਰ ਨਿਯੰਤਰਣ ਰੱਖ ਸਕਦੇ ਹਾਂ ਤਾਂ ਅਸੀਂ ਇਸਨੂੰ ਹੋਰ ਸਿਸਟਮਾਂ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹਾਂ।
- **ਬਾਹਰੀ ਡੇਟਾ**। ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਹੋਰ ਸਰੋਤਾਂ ਤੋਂ ਡੇਟਾ ਚੈਟ ਸੰਦਰਭ ਵਿੱਚ ਵਰਤਣ ਦੀ ਸਮਰੱਥਾ।

## ਸੰਦਰਭ ਰਾਹੀਂ ਮੁੱਦੇ ਨੂੰ ਦਰਸਾਉਣਾ

> ਅਸੀਂ ਤੁਹਾਨੂੰ ਸਲਾਹ ਦਿੰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਹੇਠ ਦਿੱਖਾਇਆ ਨੋਟਬੁੱਕ [included notebook](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ਵਰਤੋਂ ਜੇ ਤੁਸੀਂ ਹੇਠ ਲਿਖੇ ਸੰਦਰਭ ਨੂੰ ਚਲਾ ਕੇ ਦੇਖਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਤੁਸੀਂ ਸਿਰਫ ਪੜ੍ਹ ਕੇ ਵੀ ਸਮਝ ਸਕਦੇ ਹੋ ਕਿਉਂਕਿ ਅਸੀਂ ਇੱਕ ਸਮੱਸਿਆ ਦਰਸਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ ਜਿੱਥੇ ਫੰਕਸ਼ਨਾਂ ਸਮੱਸਿਆ ਨੂੰ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

ਆਓ ਇੱਕ ਉਦਾਹਰਨ ਵੇਖੀਏ ਜੋ ਜਵਾਬ ਫਾਰਮੈਟ ਸਮੱਸਿਆ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ:

ਮੰਨ ਲਓ ਅਸੀਂ ਵਿਦਿਆਰਥੀ ਡੇਟਾ ਦਾ ਇੱਕ ਡੇਟਾਬੇਸ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਅਸੀਂ ਉਨ੍ਹਾਂ ਨੂੰ ਸਹੀ ਕੋਰਸ ਸਿਫਾਰਿਸ਼ ਕਰ ਸਕੀਏ। ਥੱਲੇ ਦੋ ਵਿਦਿਆਰਥੀਆਂ ਦੇ ਵੇਰਵੇ ਦਿੱਤੇ ਗਏ ਹਨ ਜੋ ਡੇਟਾ ਵਿੱਚ ਕਾਫੀ ਮਿਲਦੇ ਹਨ।

1. ਸਾਡੀ Azure OpenAI ਸਰੋਤ ਨਾਲ ਕਨੈਕਸ਼ਨ ਬਣਾਓ:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # ਇਹ ਵੀ ਡਿਫਾਲਟ ਹੈ, ਇਸਨੂੰ ਛੱਡਿਆ ਜਾ ਸਕਦਾ ਹੈ
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   ਹੇਠਲੇ ਪਾਇਥਨ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਆਪਣੀ Azure OpenAI ਕਨੈਕਸ਼ਨ ਲਈ `api_type`, `api_base`, `api_version` ਅਤੇ `api_key` ਸੈਟ ਕਰ ਰਹੇ ਹਾਂ।

1. ਦੋ ਵਿਦਿਆਰਥੀ ਵੇਰਵੇ ਤਿਆਰ ਕਰੋ ਜਿਨ੍ਹਾਂ ਦਾ ਨਾਂ `student_1_description` ਅਤੇ `student_2_description` ਹੈ।

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   ਅਸੀਂ ਉਪਰ ਦਿੱਤੇ ਵੇਰਵੇ LLM ਨੂੰ ਭੇਜ ਕੇ ਡੇਟਾ ਪਾਰਸ ਕਰਵਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ। ਇਹ ਡੇਟਾ ਬਾਅਦ ਵਿੱਚ ਸਾਡੇ ਐਪ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ ਐਪੀਆਈ ਨੂੰ ਭੇਜਿਆ ਜਾਂ ਡੇਟਾਬੇਸ ਵਿੱਚ ਸੰਗ੍ਰਹਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

1. ਸੋਚੀਏ ਪੰਜਾਬੀ ਆਮ ਪ੍ਰੰਪਟ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿੰਨ੍ਹਾਂ ਵਿੱਚ ਅਸੀਂ LLM ਨੂੰ ਦੱਸਦੇ ਹਾਂ ਕਿ ਸਾਨੂੰ ਕਿਹੜੀ ਜਾਣਕਾਰੀ ਚਾਹੀਦੀ ਹੈ:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   ਉਪਰੋਕਤ ਪ੍ਰੰਪਟ LLM ਨੂੰ ਇਹ ਸਿਖਾਉਂਦੇ ਹਨ ਕਿ ਜਾਣਕਾਰੀ ਕੱਢ ਕੇ ਜਵਾਬ JSON ਫਾਰਮੈਟ ਵਿੱਚ ਦੇਣਾ ਹੈ।

1. ਪ੍ਰੰਪਟ ਤੇ Azure OpenAI ਨਾਲ ਸੰਪਰਕ ਸੈੱਟ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ ਹੁਣ `openai.ChatCompletion` ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਪ੍ਰੰਪਟ LLM ਨੂੰ ਭੇਜਾਂਗੇ। ਅਸੀਂ ਪ੍ਰੰਪਟ ਨੂੰ `messages` ਵੈਰੀਏਬਲ ਵਿੱਚ ਰੱਖਦੇ ਹਾਂ ਅਤੇ ਰੋਲ ਨੂੰ `user` ਦੇਂਦੇ ਹਾਂ। ਇਹ ਇੱਕ ਯੂਜ਼ਰ ਵਲੋਂ ਚੈਟਬੋਟ ਨੂੰ ਲਿਖੇ ਗਏ ਸੁਨੇਹੇ ਦੀ ਨਕਲ ਕਰਨ ਲਈ ਹੈ।

   ```python
   # ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਤੋਂ ਜਵਾਬ
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # ਦੂਜੇ ਪ੍ਰਾਂਪਟ ਤੋਂ ਜਵਾਬ
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

ਹੁਣ ਅਸੀਂ ਦੋਹਾਂ ਬੇਨਤੀਆਂ ਨੂੰ LLM ਨੂੰ ਭੇਜ ਕੇ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖ ਸਕਦੇ ਹਾਂ: `openai_response1['choices'][0]['message']['content']`।

1. ਆਖਿਰਕਾਰ, ਅਸੀਂ ਜਵਾਬ ਨੂੰ JSON ਫਾਰਮੈਟ ਵਿੱਚ ਤਬਦੀਲ ਕਰਨ ਲਈ `json.loads` ਕਾਲ ਕਰਾਂਗੇ:

   ```python
   # ਜਵਾਬ ਨੂੰ ਇੱਕ JSON ਓਬਜੈਕਟ ਵਜੋਂ ਲੋਡ ਕਰਨਾ
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   ਜਵਾਬ 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   ਜਵਾਬ 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   ਜਦੋਂਕਿ ਪ੍ਰੰਪਟ ਇੱਕੋ ਜਿਹੇ ਹਨ ਅਤੇ ਵੇਰਵੇ ਮਿਲਦੇ-ਜੁਲਦੇ ਹਨ, ਅਸੀਂ ਵੇਖਦੇ ਹਾਂ ਕਿ `Grades` ਗੁਣधਰੂਪ ਵੱਖ-ਵੱਖ ਫਾਰਮੈਟ ਵਿੱਚ ਹਨ, ਜਿਵੇਂ ਕਈ ਵਾਰੀ `3.7` ਜਾਂ `3.7 GPA` ਮਿਲਦਾ ਹੈ।

   ਇਹ ਨਤੀਜਾ ਇਸ ਕਾਰਨ ਹੈ ਕਿ LLM ਨਾ-ਸੰਰਚਿਤ ਡੇਟਾ ਲੈਂਦਾ ਹੈ ਜੋ ਲਿਖੇ ਪ੍ਰੰਪਟ ਦੇ ਰੂਪ ਵਿੱਚ ਹੈ ਅਤੇ ਨਾ-ਸੰਰਚਿਤ ਡੇਟਾ ਮੁੜ ਭੇਜਦਾ ਹੈ। ਸਾਨੂੰ ਇਕ ਸੰਰਚਿਤ ਫਾਰਮੈਟ ਦੀ ਲੋੜ ਹੈ ਤਾਂ ਜੋ ਸਾਨੂੰ ਪਤਾ ਚੱਲੇ ਕਿ ਡੇਟਾ ਸੰਗ੍ਰਹਿਤ ਕਰਨ ਜਾਂ ਵਰਤਣ ਸਮੇਂ ਕੀ ਉਮੀਦ ਕਰਨੀ ਹੈ।

ਤਾਂ ਫਿਰ ਅਸੀਂ ਫਾਰਮੈਟਿੰਗ ਦੀ ਸਮੱਸਿਆ ਕਿਵੇਂ ਹੱਲ ਕਰੀਏ? ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਸੀਂ ਇਹ ਸੁਨਿਸ਼ਚਿਤ ਕਰ ਸਕਦੇ ਹਾਂ ਕਿ ਸਾਨੂੰ ਮੁੜ ਸੰਰਚਿਤ ਡੇਟਾ ਮਿਲੇ। ਜਦੋਂ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, LLM ਹਕੀਕਤ ਵਿੱਚ ਕਿਸੇ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਜਾਂ ਚਲਾਉਂਦਾ ਨਹੀਂ। ਇਸ ਦੀ ਥਾਂ, ਅਸੀਂ LLM ਵਾਸਤੇ ਇੱਕ ਸੌਚਨਾ ਤਿਆਰ ਕਰਦੇ ਹਾਂ ਜਿਸਨੂੰ ਉਹ ਆਪਣੇ ਜਵਾਬਾਂ ਲਈ ਫਾਲੋ ਕਰਦਾ ਹੈ। ਫਿਰ ਅਸੀਂ ਉਹ ਸੰਰਚਿਤ ਜਵਾਬਾਂ ਜਾਣਦੇ ਹਾਂ ਕਿ ਕਿਹੜਾ ਫੰਕਸ਼ਨ ਸਾਡੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਚਲਾਉਣਾ ਹੈ।

![function flow](../../../translated_images/pa/Function-Flow.083875364af4f4bb.webp)

ਫਿਰ ਅਸੀਂ ਫੰਕਸ਼ਨ ਤੋਂ ਪ੍ਰਾਪਤ ਕੀਤੀ ਚੀਜ਼ ਲੈ ਕੇ ਇਸਨੂੰ ਮੁੜ LLM ਨੂੰ ਭੇਜ ਸਕਦੇ ਹਾਂ। LLM ਫਿਰ ਯੂਜ਼ਰ ਦੀ ਪੁੱਛਤਾਛ ਦਾ ਜਵਾਬ ਕਦਰ ਵਿੱਚ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਦੇਵੇਗਾ।

## ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਲਈ ਵਰਤੋਂ ਕੇਸ

ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਬਹੁਤ ਸਾਰੇ ਵਰਤੋਾਂ ਵਿੱਚ ਤੁਹਾਡੇ ਐਪ ਨੂੰ ਸੁਧਾਰ ਸਕਦੀਆਂ ਹਨ ਜਿਵੇਂ:

- **ਬਾਹਰੀ ਟੂਲ ਕਾਲ ਕਰਨਾ**। ਚੈਟਬੋਟ ਯੂਜ਼ਰਾਂ ਦੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਹੁੰਦੇ ਹਨ। ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਨਾਲ, ਚੈਟਬੋਟ ਯੂਜ਼ਰਾਂ ਦੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਕਿਸੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਵਰਤ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਣ ਵਜੋਂ, ਇੱਕ ਵਿਦਿਆਰਥੀ ਚੈਟਬੋਟ ਨੂੰ ਕਹਿ ਸਕਦਾ ਹੈ "ਮੇਰੇ ਅਧਿਆਪਕ ਨੂੰ ਈਮੇਲ ਭੇਜੋ ਕਿ ਮੈਨੂੰ ਇਸ ਵਿਸ਼ੇ ਵਿੱਚ ਹੋਰ ਸਹਾਇਤਾ ਦੀ ਲੋੜ ਹੈ"। ਇਹ `send_email(to: string, body: string)` ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

- **API ਜਾਂ ਡੇਟਾਬੇਸ ਕ്വੈਰੀ ਬਣਾਉਣਾ**। ਯੂਜ਼ਰ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਣਕਾਰੀ ਲੱਭ ਸਕਦੇ ਹਨ ਜੋ ਇੱਕ ਫਾਰਮੈਟੀਡ ਕੌਰੀ ਜਾਂ API ਬੇਨਤੀ ਵਿੱਚ ਬਦਲੀ ਜਾਂਦੀ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ ਇੱਕ ਅਧਿਆਪਕ ਪੁੱਛ ਸਕਦਾ ਹੈ "ਕੌਣ ਵਿਦਿਆਰਥੀਆਂ ਨੇ ਆਖਰੀ ਅਸਾਈਨਮੈਂਟ ਪੂਰਾ ਕੀਤਾ?" ਜੋ `get_completed(student_name: string, assignment: int, current_status: string)` ਫੰਕਸ਼ਨ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

- **ਸੰਰਚਿਤ ਡੇਟਾ ਬਣਾਉਣਾ**। ਯੂਜ਼ਰ ਇੱਕ ਲੰਮਾ ਟੈਕਸਟ ਜਾਂ CSV ਲੈ ਕੇ LLM ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਕੱਦ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਣ ਲਈ, ਇੱਕ ਵਿਦਿਆਰਥੀ ਅਮਨ ਸਮਝੌਤਿਆਂ ਬਾਰੇ ਵਿਕੀਪੀਡੀਆ ਆਰਟੀਕਲ ਦਾ ਡੇਟਾ ਐਲਐਲਐਮ ਨਾਲ ਕੱਢ ਕੇ AI ਫਲੈਸ਼ਕਾਰਡ ਬਣਾ ਸਕਦਾ ਹੈ। ਇਹ `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਆਪਣਾ ਪਹਿਲਾ ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉਣਾ

ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ 3 ਮੁੱਖ ਕਦਮ ਸ਼ਾਮਿਲ ਹਨ:

1. ਆਪਣੀਆਂ ਫੰਕਸ਼ਨਾਂ ਦੀ ਸੂਚੀ ਅਤੇ ਇੱਕ ਯੂਜ਼ਰ ਸੁਨੇਹਾ ਨਾਲ ਚੈਟ ਕંપਲੀਸ਼ਨ API ਨੂੰ ਕਾਲ ਕਰਨਾ।
2. ਮਾਡਲ ਦੇ ਜਵਾਬ ਨੂੰ ਪੜ੍ਹ ਕੇ ਕੋਈ ਕਾਰਵਾਈ ਕਰਨੀ ਜਿਵੇਂ ਕਿ ਫੰਕਸ਼ਨ ਜਾਂ API ਕਾਲ ਨੂੰ ਚਲਾਉਣਾ।
3. ਆਪਣੀ ਫੰਕਸ਼ਨ ਵੱਲੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨਾਲ ਮੁੜ ਚੈਟ ਕંપਲੀਸ਼ਨ API ਨੂੰ ਕਾਲ ਕਰ ਕੇ ਉਹ ਜਾਣਕਾਰੀ ਯੂਜ਼ਰ ਨੂੰ ਜਵਾਬ ਦੇਣ ਲਈ ਵਰਤਣਾ।

![LLM Flow](../../../translated_images/pa/LLM-Flow.3285ed8caf4796d7.webp)

### ਕਦਮ 1 - ਸੁਨੇਹੇ ਬਣਾਉਣਾ

ਪਹਿਲਾ ਕਦਮ ਯੂਜ਼ਰ ਸੁਨੇਹਾ ਬਣਾਉਣਾ ਹੈ। ਇਹ ਮੁੜਗੈਰੈਂਟੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਉਦਾਹਰਣ ਵਜੋਂ ਕਿਸੇ ਟੈਕਸਟ ਇਨਪੁੱਟ ਦੇ ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਂ ਤੁਸੀਂ ਇਹਥੇ ਮੁੱਲ ਦੇਂਦੇ ਹੋ। ਜੇ ਇਹ ਤੁਸੀਂ ਪਹਿਲੀ ਵਾਰੀ Chat Completions API ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਸਾਨੂੰ `role` ਅਤੇ `content` ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਲੋੜੀਦਾ ਹੈ।

`role` ਹੋ ਸਕਦਾ ਹੈ `system` (ਨਿਯਮ ਬਣਾਉਂਦਾ), `assistant` (ਮਾਡਲ) ਜਾਂ `user` (ਅੰਤ-ਯੂਜ਼ਰ)। ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਲਈ, ਅਸੀਂ ਇਸਨੂੰ `user` ਦੇ ਤੌਰ ਤੇ ਤੈਅ ਕਰਾਂਗੇ ਅਤੇ ਇੱਕ ਉਦਾਹਰਣ ਸਵਾਲ ਦੇਵਾਂਗੇ।

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

ਵੱਖ-ਵੱਖ ਰੋਲ ਦੇ ਕੇ LLM ਨੂੰ ਇਹ ਸਪਸ਼ਟ ਹੁੰਦਾ ਹੈ ਕਿ ਇਹ ਸਿਸਟਮ ਕੁਝ ਕਹਿ ਰਿਹਾ ਹੈ ਜਾਂ ਯੂਜ਼ਰ, ਜਿਸ ਨਾਲ ਗੱਲਬਾਤ ਦਾ ਇਤਿਹਾਸ ਬਣਾਉਣਾ ਆਸਾਨ ਹੁੰਦਾ ਹੈ ਜੋ LLM ਬਣਾ ਸਕਦਾ ਹੈ।

### ਕਦਮ 2 - ਫੰਕਸ਼ਨ ਤਿਆਰ ਕਰਨਾ

ਅਗਲਾ, ਅਸੀਂ ਇੱਕ ਫੰਕਸ਼ਨ ਅਤੇ ਉਸ ਫੰਕਸ਼ਨ ਦੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ। ਅਸੀਂ ਇੱਥੇ ਸਿਰਫ ਇੱਕ ਫੰਕਸ਼ਨ `search_courses` ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ ਪਰ ਤੁਸੀਂ ਕਈ ਫੰਕਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ।

> **ਮਹਤੱਵਪੂਰਨ** : ਫੰਕਸ਼ਨ ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਿੱਚ LLM ਨੂੰ ਸ਼ਾਮਿਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਇਹ ਤੁਹਾਡੇ ਉਪਲਬਧ ਟੋਕਨਾਂ ਦੇ ਮਾਤਰਾ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੁੰਦੇ ਹਨ।

ਥੱਲੇ, ਅਸੀਂ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਆਈਟਮਾਂ ਦੀ ਅਰੇ ਦੇ ਤੌਰ ਤੇ ਬਣਾਉਂਦੇ ਹਾਂ। ਹਰ ਆਈਟਮ ਇੱਕ ਫੰਕਸ਼ਨ ਹੈ ਜਿਸਦੇ ਦਿੱਤੇ ਗਏ ਗੁਣ ਹਨ: `name`, `description` ਅਤੇ `parameters`:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

ਆਓ ਹਰੇਕ ਫੰਕਸ਼ਨ ਇੰਸਟੈਂਸ ਨੂੰ ਹੇਠਾਂ ਵਿਸਥਾਰ ਨਾਲ ਸਮਝੀਏ:

- `name` - ਫੰਕਸ਼ਨ ਦਾ ਨਾਂ ਜੋ ਅਸੀਂ ਕਾਲ ਕਰਵਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ।
- `description` - ਇਹ ਫੰਕਸ਼ਨ ਦੀ ਕਾਰਵਾਈ ਦਾ ਵੇਰਵਾ ਹੈ। ਇੱਥੇ ਸਪਸ਼ਟਤਾ ਅਤੇ ਵਿਸਥਾਰ ਮਹੱਤਵਪੂਰਨ ਹੈ।
- `parameters` - ਮੁੱਲਾਂ ਅਤੇ ਫਾਰਮੈਟਾਂ ਦੀ ਸੂਚੀ ਜੋ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਮਾਡਲ ਆਪਣੀ ਪ੍ਰਤੀਕ੍ਰਿਆ ਵਿੱਚ ਤਿਆਰ ਕਰੇ। ਪੈਰਾਮੀਟਰ ਆਰੇ ਵਿੱਚ ਆਈਟਮ ਹੁੰਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਹੇਠ ਲਿਖੇ ਗੁਣ ਹਨ:
  1. `type` - ਜਿਸ ਡੇਟਾ ਕਿਸਮ ਵਿੱਚ ਗੁਣਧਰੂਪ ਸਟੋਰ ਕੀਤਾ ਜਾਵੇਗਾ।
  2. `properties` - ਵਿਸ਼ੇਸ਼ ਮੁੱਲਾਂ ਦੀ ਸੂਚੀ ਜੋ ਮਾਡਲ ਆਪਣੀ ਪ੍ਰਤੀਕ੍ਰਿਆ ਲਈ ਵਰਤੇਗਾ
      1. `name` - ਕੁੰਜੀ ਜੋ ਗੁਣਧਰੂਪ ਦੇ ਨਾਮ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ ਜਿਵੇਂ ਕਿ `product`।
      2. `type` - ਇਸ ਗੁਣਧਰੂਪ ਦਾ ਡੇਟਾ ਟਾਈਪ ਜਿਵੇਂ ਕਿ `string`।
      3. `description` - ਇਸ ਵਿਸ਼ੇਸ਼ ਗੁਣਧਰੂਪ ਦਾ ਵਰਣਨ।

ਇੱਕ ਵਿਕਲਪੀ ਗੁਣਧਰੂਪ `required` ਵੀ ਹੁੰਦਾ ਹੈ - ਜੋ ਫੰਕਸ਼ਨ ਕਾਲ ਪੂਰਾ ਕਰਨ ਲਈ ਲਾਜ਼ਮੀ ਹੈ।

### ਕਦਮ 3 - ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨਾ

ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਹੁਣ ਸਾਨੂੰ ਇਸਨੂੰ Chat Completion API ਕਾਲ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨਾ ਹੈ। ਅਸੀਂ ਇਹ `functions` ਨੂੰ ਬੇਨਤੀ ਵਿਚ ਸ਼ਾਮਿਲ ਕਰਕੇ ਕਰਦੇ ਹਾਂ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ `functions=functions` ਹੁੰਦਾ ਹੈ।

ਇਸਦੇ ਨਾਲ ਇੱਕ ਵਿਕਲਪ ਹੈ `function_call` ਨੂੰ `auto` ਤੇ ਸੈੱਟ ਕਰਨ ਦਾ। ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ ਅਸੀਂ LLM ਨੂੰ ਇਹ ਫੈਸਲਾ ਕਰਨ ਦਿੰਦੇ ਹਾਂ ਕਿ ਕਿਸ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਹੈ ਯੂਜ਼ਰ ਸੁਨੇਹੇ ਦੇ ਆਧਾਰ `ਵਜੋਂ` ਨਾ ਕਿ ਅਸੀਂ ਖੁਦ ਇਹ ਐਸਾਈਂ ਕਰੀਏ।

ਥੱਲੇ ਕੁਝ ਕੋਡ ਹੈ ਜਿਥੇ ਅਸੀਂ `ChatCompletion.create` ਕਾਲ ਕਰਦੇ ਹਾਂ, ਦੇਖੋ ਕਿਵੇਂ ਅਸੀਂ `functions=functions` ਅਤੇ `function_call="auto"` ਸੈੱਟ ਕੀਤੇ ਹਨ ਅਤੇ LLM ਨੂੰ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦਾ ਚੋਣ ਦਿੱਤੀ ਹੈ:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

ਹੁਣ ਲੌਟਣ ਵਾਲਾ ਜਵਾਬ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਖਦਾ ਹੈ:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

ਅਸੀਂ ਇੱਥੇ ਵੇਖ ਸਕਦੇ ਹਾਂ ਕਿ `search_courses` ਫੰਕਸ਼ਨ ਕਿਵੇਂ ਕਾਲ ਕੀਤਾ ਗਿਆ ਅਤੇ ਕਿਸ ਤਰ੍ਹਾਂ ਦੇ ਆਰਗੁਮੈਂਟ ਦਿੱਤੇ ਗਏ ਜੋ JSON ਜਵਾਬ ਵਿੱਚ `arguments` ਗੁਣਧਰੂਪ ਹੇਠਾਂ ਦਿੱਤੇ ਹਨ।

ਨਤੀਜਾ ਇਹ ਸੀ ਕਿ LLM ਮੈਸੇਜਿਸ ਪੈਰਾਮੀਟਰ ਵਿੱਚ ਦਿੱਤੀ ਗਈ ਮੁੱਲ ਤੋਂ ਡੇਟਾ ਕੱਢ ਕਰ ਫੰਕਸ਼ਨ ਦੇ ਆਰਗੁਮੈਂਟਾਂ ਨਾਲ ਮਿਲਾਉਣ ਵਿੱਚ ਕਾਮਯਾਬ ਹੋਇਆ। ਹੇਠਾਂ `messages` ਦੀ ਮੁੱਲ ਦਾ ਯਾਦ ਦਵਾਉਣਾ ਹੈ:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

ਜਿਵੇਂ ਕਿ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, `student`, `Azure` ਅਤੇ `beginner` ਨੂੰ `messages` ਵਿੱਚੋਂ ਕੱਡ ਕੇ ਫੰਕਸ਼ਨ ਲਈ ਇਨਪੁਟ ਵਜੋਂ ਵਰਤਿਆ ਗਿਆ। ਇਸ ਤਰ੍ਹਾਂ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਪ੍ਰੰਪਟ ਵਿੱਚੋਂ ਜਾਣਕਾਰੀ ਕੱਢਣ ਲਈ ਵਧੀਆ ਹੈ ਪਰ ਇਹ ਵੀ ਕਿ LLM ਨੂੰ ਬਣਤਰ ਦੇਣ ਅਤੇ ਦੁਬਾਰਾ ਵਰਤੋਂ ਯੋਗ ਫੰਕਸ਼ਨ ਬਣਾਉਣ ਵਾਲਾ ਤਰੀਕਾ ਹੈ।

ਹੁਣ, ਅਸੀਂ ਵੇਖਦੇ ਹਾਂ ਕਿ ਇਸ ਨੂੰ ਸਾਡੇ ਐਪ ਵਿੱਚ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਨੂੰ ਜੋੜਨਾ

LLM ਤੋਂ ਪ੍ਰਾਪਤ ਸੰਰਚਿਤ ਜਵਾਬ ਦੀ ਜਾਂਚ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ ਹੁਣ ਇਸਨੂੰ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹਾਂ।

### ਫਲੋ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨਾ

ਇਸ ਨੂੰ ਆਪਣੇ ਐਪ ਵਿੱਚ ਜੋੜਨ ਲਈ, ਆਓ ਹੇਠਾਂ ਦੱਸੀ ਗਈਆਂ ਕਦਮਾਂ ਨੂੰ ਅਪਣਾਈਏ:

1. ਪਹਿਲਾਂ, OpenAI ਸੇਵਾਵਾਂ ਨੂੰ ਕਾਲ ਕਰੋ ਅਤੇ ਸੁਨੇਹਾ ਨੂੰ ਇੱਕ ਵੈਰੀਏਬਲ `response_message` ਵਿੱਚ ਸਟੋਰ ਕਰੋ।

   ```python
   response_message = response.choices[0].message
   ```

1. ਹੁਣ ਅਸੀਂ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ ਜੋ Microsoft Learn API ਨੂੰ ਕਾਲ ਕਰਕੇ ਕੋਰਸਾਂ ਦੀ ਸੂਚੀ ਲੱਭੇਗਾ:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   ਧਿਆਨ ਦਿਓ ਕਿ ਅਸੀਂ ਹੁਣ ਇੱਕ ਵਾਸਤਵਿਕ ਪਾਇਥਨ ਫੰਕਸ਼ਨ ਬਣਾਉਂਦੇ ਹਾਂ ਜੋ `functions` ਵੈਰੀਏਬਲ ਵਿੱਚ ਦਿੱਤੇ ਫੰਕਸ਼ਨ ਦੇ ਨਾਮਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ। ਅਸੀਂ ਅਸਲ ਵਿੱਚ ਬਾਹਰੀ API ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ ਤਾਂ ਜੋ ਲੋੜੀਂਦਾ ਡੇਟਾ ਪ੍ਰਾਪਤ ਕਰ ਸਕੀਏ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ Microsoft Learn API ਖਿਲਾਫ ਜਾਂਦੇ ਹਾਂ ਤਾਂ ਜੋ ਟਰੈਨਿੰਗ ਮੋਡਿਊਲ ਲੱਭ ਸਕੀਏ।

ਠੀਕ ਹੈ, ਤਾਂ ਅਸੀਂ `functions` ਵੈਰੀਏਬਲ ਬਣਾਈ ਅਤੇ ਇੱਕ ਪਾਇਥਨ ਫੰਕਸ਼ਨ ਵੀ ਬਣਾਇਆ, ਹੁਣ ਅਸੀਂ LLM ਨੂੰ ਦੱਸੋਂ ਕਿ ਇਨ੍ਹਾਂ ਦੋਹਾਂ ਨੂੰ ਕਿਵੇਂ ਮੇਲ ਕਰਨਾ ਹੈ ਤਾਂ ਜੋ ਸਾਡੇ ਪਾਇਥਨ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰ ਸਕੀਏ?

1. ਦੇਖਣ ਲਈ ਕਿ ਸਾਨੂੰ ਪਾਇਥਨ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਨਹੀਂ, ਅਸੀਂ LLM ਦੇ ਜਵਾਬ ਨੂੰ ਦੇਖਦੇ ਹਾਂ ਕਿ ਕੀ `function_call` ਇਸ ਵਿੱਚ ਹੈ ਅਤੇ ਉਸ ਫੰਕਸ਼ਨ ਨੂੰ ਜੋ ਤਰਸਾਇਆ ਗਿਆ ਹੈ ਕਾਲ ਕਰਦੇ ਹਾਂ। ਹੇਠਾਂ ਇਸਕੀ ਜਾਂਚ ਕਰਨ ਦੇ ਤਰੀਕੇ ਦਿੱਤੇ ਗਏ ਹਨ:

   ```python
   # ਦੇਖੋ ਕਿ ਮਾਡਲ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੁੰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰੋ।
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸਹਾਇਕ ਦੀ ਜਵਾਬ ਅਤੇ ਫੰਕਸ਼ਨ ਦੀ ਜਵਾਬ ਜੁੜੋ
    messages.append( # ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸਹਾਇਕ ਦੀ ਜਵਾਬ ਜੁੜ ਰਹੀ ਹੈ
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਫੰਕਸ਼ਨ ਦੀ ਜਵਾਬ ਜੁੜ ਰਹੀ ਹੈ
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   ਇਹ ਤਿੰਨ ਲਾਈਨਾਂ ਯਕੀਨ ਬਣਾਉਂਦੀਆਂ ਹਨ ਕਿ ਅਸੀਂ ਫੰਕਸ਼ਨ ਦਾ ਨਾਂ, ਆਰਗੁਮੈਂਟ ਕੱਢ ਕੇ ਫ਼ਰਮਾਇਸ਼ ਕਰਦੇ ਹਾਂ:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   ਹੇਠਾਂ ਸਾਡਾ ਕੋਡ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ ਆਉਣ ਵਾਲਾ ਪ੍ਰਿੰਟ ਹੈ:

   **ਆਉਟਪੁੱਟ**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. ਹੁਣ ਅਸੀਂ ਤਬਦੀਲ ਕੀਤਾ ਸੁਨੇਹਾ `messages` LLM ਨੂੰ ਭੇਜਾਂਗੇ ਤਾਂ ਜੋ ਅਸੀਂ ਇੱਕ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਾਲਾ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕੀਏ ਨਾ ਕਿ API JSON ਫਾਰਮੈਟਡ ਜਵਾਬ।

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # GPT ਤੋਂ ਇੱਕ ਨਵਾਂ ਜਵਾਬ ਲਵੋ ਜਿੱਥੇ ਇਹ ਫੰਕਸ਼ਨ ਜਵਾਬ ਨੂੰ ਦੇਖ ਸਕਦਾ ਹੈ


   print(second_response.choices[0].message)
   ```

   **ਆਉਟਪੁੱਟ**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## ਅਸਾਈਨਮੈਂਟ

ਆਪਣੀ Azure OpenAI Function Calling ਦੀ ਸਿੱਖਿਆ جاري ਰੱਖਣ ਲਈ, ਤੁਸੀਂ ਇਨ੍ਹਾਂ ਚੀਜ਼ਾਂ 'ਤੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ:

- ਫੰਕਸ਼ਨ ਦੇ ਹੋਰ ਪੈਰਾਮੀਟਰ ਬਣਾਉ ਜੋ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨੂੰ ਹੋਰ ਕੋਰਸ ਲੱਭਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।
- ਇੱਕ ਹੋਰ ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉ ਜੋ ਸਿੱਖਣ ਵਾਲੇ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਰਗੀਆਂ ਹੋਰ ਜਾਣਕਾਰੀਆਂ ਲੈਂਦੀ ਹੋਵੇ।
- ਰੂਟੀਨ ਬਣਾਉ ਜੋ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ/ਜਾਂ API ਕਾਲ ਜਦੋਂ ਕੋਈ ਯੋਗ ਕੋਰਸ ਵਾਪਸ ਨਾ ਕਰਨ ਤਾਂ ਤਰਤੀਬ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਅਮਲ ਕਰੇ।
ਸੰਕੇਤ: ਇਹ ਡਾਟਾ ਕਿਵੇਂ ਅਤੇ ਕਿੱਥੇ ਉਪਲਬਧ ਹੈ, ਦੇਖਣ ਲਈ [Learn API reference documentation](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) ਪੱਨੇ ਦਾ ਪਾਲਣਾ ਕਰੋ।

## ਸ਼ਾਨਦਾਰ ਕੰਮ! ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਜਰੂਰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ Generative AI ਗਿਆਨ ਨੂੰ ਅੱਗੇ ਵਧਾ ਸਕੋ!

ਪਾਠ 12 ਵੱਲ ਜਾਓ, ਜਿੱਥੇ ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ UX ਡਿਜ਼ਾਈਨ ਕਰਨਾ](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ਹੈ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->