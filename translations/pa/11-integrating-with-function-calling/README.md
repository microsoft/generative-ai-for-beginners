<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-06-25T19:50:41+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "pa"
}
-->
# ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨਾਲ ਇੱਕੀਕਰਨ

ਤੁਸੀਂ ਪਿਛਲੇ ਪਾਠਾਂ ਵਿੱਚ ਕਾਫ਼ੀ ਕੁਝ ਸਿੱਖਿਆ ਹੈ। ਹਾਲਾਂਕਿ, ਅਸੀਂ ਹੋਰ ਸੁਧਾਰ ਕਰ ਸਕਦੇ ਹਾਂ। ਕੁਝ ਚੀਜ਼ਾਂ ਜਿਨ੍ਹਾਂ ਨੂੰ ਅਸੀਂ ਸੰਬੋਧਿਤ ਕਰ ਸਕਦੇ ਹਾਂ ਉਹ ਇਹ ਹਨ ਕਿ ਅਸੀਂ ਜਵਾਬ ਦੇ ਡਾਢੇ ਨੂੰ ਹੋਰ ਸਥਿਰ ਫਾਰਮੈਟ ਵਿੱਚ ਕਿਵੇਂ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ ਤਾਂ ਕਿ ਇਹ ਜਵਾਬ ਨਾਲ ਹੇਠਾਂ ਕੰਮ ਕਰਨ ਵਿੱਚ ਸੌਖਾ ਬਣ ਸਕੇ। ਇਸ ਤੋਂ ਇਲਾਵਾ, ਅਸੀਂ ਹੋਰ ਸਰੋਤਾਂ ਤੋਂ ਡਾਟਾ ਜੋੜਨਾ ਚਾਹੁੰਦੇ ਹਾਂ ਤਾਂ ਕਿ ਸਾਡੇ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਹੋਰ ਸੰਮ੍ਰਿਧ ਕੀਤਾ ਜਾ ਸਕੇ।

ਉਪਰੋਕਤ ਸਮੱਸਿਆਵਾਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸੰਬੋਧਨ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ।

## ਪਰੇਚਾ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ:

- ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਕੀ ਹੈ ਅਤੇ ਇਸਦੇ ਉਪਯੋਗ ਮਾਮਲੇ ਨੂੰ ਸਮਝਾਉਣਾ।
- Azure OpenAI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉਣਾ।
- ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਫੰਕਸ਼ਨ ਕਾਲ ਨੂੰ ਕਿਵੇਂ ਇੱਕੀਕਰਿਤ ਕਰਨਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਦੇ ਉਦੇਸ਼ ਨੂੰ ਸਮਝਾਉਣਾ।
- Azure OpenAI ਸਰਵਿਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫੰਕਸ਼ਨ ਕਾਲ ਸੈਟਅਪ ਕਰਨਾ।
- ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਉਪਯੋਗ ਮਾਮਲੇ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਡਿਜ਼ਾਇਨ ਕਰਨਾ।

## ਸਨੇਰੀਓ: ਸਾਡੇ ਚੈਟਬੋਟ ਨੂੰ ਫੰਕਸ਼ਨਾਂ ਨਾਲ ਸੁਧਾਰਨਾ

ਇਸ ਪਾਠ ਲਈ, ਅਸੀਂ ਆਪਣੀ ਸਿੱਖਿਆ ਸਟਾਰਟਅਪ ਲਈ ਇੱਕ ਫੀਚਰ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ ਟੈਕਨੀਕਲ ਕੋਰਸਾਂ ਨੂੰ ਲੱਭਣ ਲਈ ਚੈਟਬੋਟ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਅਸੀਂ ਉਹ ਕੋਰਸਾਂ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਾਂਗੇ ਜੋ ਉਨ੍ਹਾਂ ਦੇ ਹੁਨਰ ਪੱਧਰ, ਮੌਜੂਦਾ ਭੂਮਿਕਾ ਅਤੇ ਰੁਚੀ ਦੀ ਤਕਨਾਲੋਜੀ ਦੇ ਅਨੁਕੂਲ ਹੋਣ।

ਇਸ ਸਨੇਰੀਓ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਅਸੀਂ ਇੱਕ ਕੰਬੀਨੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ:

- `Azure OpenAI` ਯੂਜ਼ਰ ਲਈ ਚੈਟ ਅਨੁਭਵ ਬਣਾਉਣ ਲਈ।
- `Microsoft Learn Catalog API` ਯੂਜ਼ਰ ਦੀ ਬੇਨਤੀ ਦੇ ਅਧਾਰ 'ਤੇ ਕੋਰਸ ਲੱਭਣ ਵਿੱਚ ਯੂਜ਼ਰਾਂ ਦੀ ਮਦਦ ਕਰਨ ਲਈ।
- `Function Calling` ਯੂਜ਼ਰ ਦੀ ਪੁੱਛਤਾਛ ਨੂੰ ਲੈਣ ਅਤੇ API ਬੇਨਤੀ ਕਰਨ ਲਈ ਇਸਨੂੰ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਭੇਜਣ ਲਈ।

ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਆਓ ਪਹਿਲੀ ਜਗ੍ਹਾ ਵਿੱਚ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਕਾਰਨ 'ਤੇ ਨਜ਼ਰ ਪਾਈਏ:

## ਕਿਉਂ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਤੋਂ ਪਹਿਲਾਂ, LLM ਤੋਂ ਜਵਾਬ ਅਸੰਰਚਿਤ ਅਤੇ ਅਸਥਿਰ ਹੁੰਦੇ ਸਨ। ਵਿਕਾਸਕਾਂ ਨੂੰ ਹਰ ਜਵਾਬ ਦੇ ਵੈਰੀਏਸ਼ਨ ਨੂੰ ਸਹਿਣ ਕਰਨ ਲਈ ਜਟਿਲ ਵੈਧਤਾ ਕੋਡ ਲਿਖਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਸੀ। ਯੂਜ਼ਰਾਂ ਨੂੰ "ਸਟਾਕਹੋਮ ਵਿੱਚ ਮੌਜੂਦਾ ਮੌਸਮ ਕੀ ਹੈ?" ਵਰਗੇ ਜਵਾਬ ਨਹੀਂ ਮਿਲ ਸਕਦੇ ਸਨ। ਇਹ ਇਸ ਲਈ ਹੈ ਕਿਉਂਕਿ ਮਾਡਲਾਂ ਨੂੰ ਉਸ ਸਮੇਂ ਦੀ ਸਿੱਖਿਆ 'ਤੇ ਸੀਮਿਤ ਕੀਤਾ ਗਿਆ ਸੀ।

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ Azure OpenAI ਸਰਵਿਸ ਦੀ ਇੱਕ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਜੋ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਸੀਮਾਵਾਂ ਨੂੰ ਪਾਰ ਕਰਨ ਲਈ:

- **ਸਥਿਰ ਜਵਾਬ ਫਾਰਮੈਟ**. ਜੇਕਰ ਅਸੀਂ ਜਵਾਬ ਦੇ ਫਾਰਮੈਟ ਨੂੰ ਬਿਹਤਰ ਤਰੀਕੇ ਨਾਲ ਨਿਯੰਤਰਿਤ ਕਰ ਸਕਦੇ ਹਾਂ ਤਾਂ ਅਸੀਂ ਹੋਰ ਸੌਖੇ ਤਰੀਕੇ ਨਾਲ ਜਵਾਬ ਨੂੰ ਹੋਰ ਸਿਸਟਮਾਂ ਵਿੱਚ ਇੱਕੀਕਰਿਤ ਕਰ ਸਕਦੇ ਹਾਂ।
- **ਬਾਹਰੀ ਡਾਟਾ**. ਇੱਕ ਚੈਟ ਸੰਦਰਭ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਹੋਰ ਸਰੋਤਾਂ ਤੋਂ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਯੋਗਤਾ।

## ਸਨੇਰੀਓ ਰਾਹੀਂ ਸਮੱਸਿਆ ਨੂੰ ਦਰਸਾਉਣਾ

> ਅਸੀਂ ਤੁਹਾਨੂੰ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਜੇਕਰ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਸਨੇਰੀਓ ਨੂੰ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ [ਸ਼ਾਮਲ ਨੋਟਬੁਕ](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) ਦੀ ਵਰਤੋਂ ਕਰੋ। ਤੁਸੀਂ ਸਿਰਫ਼ ਪੜ੍ਹ ਸਕਦੇ ਹੋ ਕਿਉਂਕਿ ਅਸੀਂ ਇੱਕ ਸਮੱਸਿਆ ਨੂੰ ਦਰਸਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ ਜਿੱਥੇ ਫੰਕਸ਼ਨ ਸਮੱਸਿਆ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

ਆਓ ਉਦਾਹਰਨ 'ਤੇ ਨਜ਼ਰ ਪਾਈਏ ਜੋ ਜਵਾਬ ਦੇ ਫਾਰਮੈਟ ਦੀ ਸਮੱਸਿਆ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ:

ਮੰਨ ਲਓ ਕਿ ਅਸੀਂ ਵਿਦਿਆਰਥੀ ਡਾਟਾ ਦੀ ਇੱਕ ਡਾਟਾਬੇਸ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਤਾਂ ਕਿ ਅਸੀਂ ਉਨ੍ਹਾਂ ਨੂੰ ਸਹੀ ਕੋਰਸ ਦੀ ਸਿਫਾਰਸ਼ ਕਰ ਸਕੀਏ। ਹੇਠਾਂ ਸਾਡੇ ਕੋਲ ਵਿਦਿਆਰਥੀਆਂ ਦੇ ਦੋ ਵੇਰਵੇ ਹਨ ਜੋ ਉਨ੍ਹਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਡਾਟਾ ਵਿੱਚ ਬਹੁਤ ਹੀ ਸਮਾਨ ਹਨ।

1. ਸਾਡੇ Azure OpenAI ਸਰੋਤ ਨਾਲ ਇੱਕ ਕਨੈਕਸ਼ਨ ਬਣਾਉ:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   ਹੇਠਾਂ ਕੁਝ Python ਕੋਡ ਹੈ ਜੋ ਸਾਡੇ ਕਨੈਕਸ਼ਨ ਨੂੰ Azure OpenAI ਨਾਲ ਸੰਰਚਿਤ ਕਰਨ ਲਈ ਹੈ ਜਿੱਥੇ ਅਸੀਂ `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description` ਸੈਟ ਕਰਦੇ ਹਾਂ।

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   ਅਸੀਂ ਉਪਰੋਕਤ ਵਿਦਿਆਰਥੀ ਵੇਰਵੇ ਨੂੰ LLM ਨੂੰ ਭੇਜਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਤਾਂ ਕਿ ਡਾਟਾ ਨੂੰ ਪਾਰਸ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ ਡਾਟਾ ਬਾਅਦ ਵਿੱਚ ਸਾਡੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ API ਨੂੰ ਭੇਜਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ ਡਾਟਾਬੇਸ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

1. ਆਓ ਦੋ ਇਕਸਾਰ ਪ੍ਰੋਮਪਟ ਬਣਾਈਏ ਜਿਸ ਵਿੱਚ ਅਸੀਂ LLM ਨੂੰ ਇਹ ਦਿਸ਼ਾ ਨਿਰਦੇਸ਼ ਦਿੰਦੇ ਹਾਂ ਕਿ ਅਸੀਂ ਕਿਹੜੀ ਜਾਣਕਾਰੀ ਵਿੱਚ ਦਿਲਚਸਪੀ ਰੱਖਦੇ ਹਾਂ:

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

   ਉਪਰੋਕਤ ਪ੍ਰੋਮਪਟ LLM ਨੂੰ ਜਾਣਕਾਰੀ ਕੱਢਣ ਅਤੇ JSON ਫਾਰਮੈਟ ਵਿੱਚ ਜਵਾਬ ਵਾਪਸ ਕਰਨ ਲਈ ਦਿਸ਼ਾ ਨਿਰਦੇਸ਼ ਦਿੰਦੇ ਹਨ।

1. ਪ੍ਰੋਮਪਟ ਅਤੇ Azure OpenAI ਨਾਲ ਕਨੈਕਸ਼ਨ ਸੈਟਅਪ ਕਰਨ ਦੇ ਬਾਅਦ, ਅਸੀਂ ਹੁਣ `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਮਪਟ ਨੂੰ LLM ਨੂੰ ਭੇਜਾਂਗੇ। ਇਹ ਇੱਕ ਯੂਜ਼ਰ ਤੋਂ ਇੱਕ ਚੈਟਬੋਟ ਨੂੰ ਲਿਖੀ ਗਈ ਸੁਨੇਹਾ ਦੀ ਨਕਲ ਕਰਨ ਲਈ ਹੈ।

   ```python
   # response from prompt one
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # response from prompt two
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

ਹੁਣ ਅਸੀਂ ਦੋਵੇਂ ਬੇਨਤੀਆਂ ਨੂੰ LLM ਨੂੰ ਭੇਜ ਸਕਦੇ ਹਾਂ ਅਤੇ ਪ੍ਰਾਪਤ ਕੀਤੇ ਗਏ ਜਵਾਬ ਦੀ ਜਾਂਚ ਇਸ ਤਰੀਕੇ ਨਾਲ ਕਰ ਸਕਦੇ ਹਾਂ `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
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

   ਹਾਲਾਂਕਿ ਪ੍ਰੋਮਪਟ ਇਕੋ ਜਿਹੇ ਹਨ ਅਤੇ ਵੇਰਵੇ ਸਮਾਨ ਹਨ, ਅਸੀਂ `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.pa.png)

We can then take what is returned from the function and send this back to the LLM. The LLM will then respond using natural language to answer the user's query.

## Use Cases for using function calls

There are many different use cases where function calls can improve your app like:

- **Calling External Tools**. Chatbots are great at providing answers to questions from users. By using function calling, the chatbots can use messages from users to complete certain tasks. For example, a student can ask the chatbot to "Send an email to my instructor saying I need more assistance with this subject". This can make a function call to `send_email(to: string, body: string)`

- **Create API or Database Queries**. Users can find information using natural language that gets converted into a formatted query or API request. An example of this could be a teacher who requests "Who are the students that completed the last assignment" which could call a function named `get_completed(student_name: string, assignment: int, current_status: string)`

- **Creating Structured Data**. Users can take a block of text or CSV and use the LLM to extract important information from it. For example, a student can convert a Wikipedia article about peace agreements to create AI flashcards. This can be done by using a function called `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Creating Your First Function Call

The process of creating a function call includes 3 main steps:

1. **Calling** the Chat Completions API with a list of your functions and a user message.
2. **Reading** the model's response to perform an action i.e. execute a function or API Call.
3. **Making** another call to Chat Completions API with the response from your function to use that information to create a response to the user.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.pa.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` ਅਤੇ ਇੱਕ ਉਦਾਹਰਣ ਸਵਾਲ ਦੇ ਮੁੱਲ ਵੇਖਦੇ ਹਾਂ।

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

ਵੱਖਰੇ ਭੂਮਿਕਾਵਾਂ ਨੂੰ ਸੌਂਪ ਕੇ, ਇਹ LLM ਲਈ ਸਪਸ਼ਟ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਕੀ ਇਹ ਸਿਸਟਮ ਕੁਝ ਕਹਿ ਰਿਹਾ ਹੈ ਜਾਂ ਯੂਜ਼ਰ, ਜਿਸ ਨਾਲ ਇੱਕ ਗੱਲਬਾਤ ਦਾ ਇਤਿਹਾਸ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਮਿਲਦੀ ਹੈ ਜਿਸ 'ਤੇ LLM ਬਣਾਉਣ ਕਰ ਸਕਦਾ ਹੈ।

### ਕਦਮ 2 - ਫੰਕਸ਼ਨ ਬਣਾਉਣਾ

ਅਗਲਾ, ਅਸੀਂ ਇੱਕ ਫੰਕਸ਼ਨ ਅਤੇ ਉਸ ਫੰਕਸ਼ਨ ਦੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ। ਅਸੀਂ ਇੱਥੇ ਸਿਰਫ ਇੱਕ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ ਜਿਸਨੂੰ `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters` ਕਿਹਾ ਜਾਂਦਾ ਹੈ:

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

ਆਓ ਹੇਠਾਂ ਹਰ ਫੰਕਸ਼ਨ ਇੰਸਟੈਂਸ ਨੂੰ ਹੋਰ ਵਿਸਥਾਰ ਵਿੱਚ ਦਰਸਾਉਂਦੇ ਹਾਂ:

- `name` - The name of the function that we want to have called.
- `description` - This is the description of how the function works. Here it's important to be specific and clear.
- `parameters` - A list of values and format that you want the model to produce in its response. The parameters array consists of items where the items have the following properties:
  1.  `type` - The data type of the properties will be stored in.
  1.  `properties` - List of the specific values that the model will use for its response
      1. `name` - The key is the name of the property that the model will use in its formatted response, for example, `product`.
      1. `type` - The data type of this property, for example, `string`.
      1. `description` - Description of the specific property.

There's also an optional property `required` - required property for the function call to be completed.

### Step 3 - Making the function call

After defining a function, we now need to include it in the call to the Chat Completion API. We do this by adding `functions` to the request. In this case `functions=functions`.

There is also an option to set `function_call` to `auto`. This means we will let the LLM decide which function should be called based on the user message rather than assigning it ourselves.

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` ਅਤੇ ਇਸ ਤਰੀਕੇ ਨਾਲ LLM ਨੂੰ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨ ਦੀ ਚੋਣ ਦੇ ਰਹੇ ਹਾਂ ਜਦੋਂ ਅਸੀਂ ਇਸ ਨੂੰ ਮੁਹੱਈਆ ਕਰਦੇ ਹਾਂ:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

ਹੁਣ ਵਾਪਸ ਆਉਣ ਵਾਲਾ ਜਵਾਬ ਇਸ ਤਰੀਕੇ ਨਾਲ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

ਇੱਥੇ ਅਸੀਂ ਵੇਖ ਸਕਦੇ ਹਾਂ ਕਿ ਫੰਕਸ਼ਨ `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` ਮੁੱਲ:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

ਜਿਵੇਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. ਹੁਣ ਅਸੀਂ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ ਜੋ Microsoft Learn API ਨੂੰ ਕੋਰਸਾਂ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਾਲ ਕਰੇਗਾ:

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

   ਨੋਟ ਕਰੋ ਕਿ ਅਸੀਂ ਹੁਣ ਇੱਕ ਅਸਲ Python ਫੰਕਸ਼ਨ ਬਣਾਉਂਦੇ ਹਾਂ ਜੋ `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` ਵਿੱਚ ਪੇਸ਼ ਕੀਤੇ ਫੰਕਸ਼ਨ ਨਾਮਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਅਤੇ ਇਸਦਾ ਹਿੱਸਾ ਹੈ ਅਤੇ ਦਰਸਾਏ ਗਏ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। ਇੱਥੇ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਚੈੱਕ ਨੂੰ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ:

   ```python
   # Check if the model wants to call a function
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # Call the function.
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


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   ਇਹ ਤਿੰਨ ਲਾਈਨਾਂ, ਫੰਕਸ਼ਨ ਨਾਮ, ਦਲੀਲਾਂ ਕੱਢਣ ਅਤੇ ਕਾਲ ਕਰਨ ਦੀ ਯਕੀਨੀਤਾ ਦਿੰਦੇ ਹਨ:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   ਹੇਠਾਂ ਸਾਡੇ ਕੋਡ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪ੍ਰਾਪਤ ਆਉਟਪੁੱਟ ਹੈ:

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

1. ਹੁਣ ਅਸੀਂ ਅਪਡੇਟ ਕੀਤੀ ਗਈ ਸੁਨੇਹਾ, `messages` ਨੂੰ LLM ਨੂੰ ਭੇਜਾਂਗੇ ਤਾਂ ਕਿ ਅਸੀਂ API JSON ਫਾਰਮੈਟ ਕੀਤੇ ਜਵਾਬ ਦੇ ਬਦਲੇ ਇੱਕ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕੀਏ।

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
         )  # get a new response from GPT where it can see the function response


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

Azure OpenAI ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੇ ਸਿੱਖਣ ਨੂੰ ਜਾਰੀ ਰੱਖਣ ਲਈ ਤੁਸੀਂ ਬਣਾਉਣ ਕਰ ਸਕਦੇ ਹੋ:

- ਫੰਕਸ਼ਨ ਦੇ ਹੋਰ ਪੈਰਾਮੀਟਰ ਜੋ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨੂੰ ਹੋਰ ਕੋਰਸ ਲੱਭਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।
- ਇੱਕ ਹੋਰ ਫੰਕਸ਼ਨ ਕਾਲ ਬਣਾਉ ਜੋ ਸਿੱਖਣ ਵਾਲੇ ਤੋਂ ਹੋਰ ਜਾਣਕਾਰੀ ਲੈਂਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਉਨ੍ਹਾਂ ਦੀ ਮੂਲ ਭਾਸ਼ਾ
- ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ/ਜਾਂ API ਕਾਲ ਸੂਟਬਲ ਕੋਰਸ ਨਾ ਵਾਪਸ ਕਰਨ ਤੇ ਗਲਤੀ ਸੰਭਾਲਣਾ

ਸੁਝਾਅ: ਇਹ ਡਾਟਾ ਕਿਵੇਂ ਅਤੇ ਕਿੱਥੇ ਉਪਲਬਧ ਹੈ ਇਹ ਦੇਖਣ ਲਈ [Learn API ਸੰਦਰਭ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) ਪੰਨਾ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਵਧੀਆ ਕੰਮ! ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਹ ਪਾਠ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਕਿ ਆਪਣੇ Generative AI ਗਿਆਨ ਨੂੰ ਉੱਚਾ ਕਰ ਸਕੀਏ!

ਪਾਠ 12 ਵੱਲ ਜਾਓ, ਜਿੱਥੇ ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [AI ਐਪਲੀਕੇਸ਼ਨ ਲਈ UX ਡਿਜ਼ਾਇਨ ਕਰਨਾ ਹੈ](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਨ ਹੋ ਸਕਦੇ ਹਨ। ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।