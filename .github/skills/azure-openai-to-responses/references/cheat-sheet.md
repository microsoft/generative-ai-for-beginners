# Responses API Cheat Sheet (Python + Azure OpenAI)

> All snippets assume `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` and `client` is already initialized.

Installed from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) (MIT).

## Client setup — API key

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Client setup — EntraID (recommended)

```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client setup

```python
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,   # or api_key=os.environ["AZURE_OPENAI_API_KEY"]
)
```

## Basic request

```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Full sync migration — before/after

Before (Chat Completions):
```python
from openai import AzureOpenAI
client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

After (Responses API):
```python
from openai import OpenAI
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Multi-turn conversation

```python
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]
response = client.responses.create(model=deployment, input=messages, max_output_tokens=400)
messages.append({"role": "assistant", "content": response.output_text})
messages.append({"role": "user", "content": "Now optimize it with memoization"})
response2 = client.responses.create(model=deployment, input=messages, max_output_tokens=400)
print(response2.output_text)
```

## Streaming (sync)

```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Streaming (async)

```python
stream = await client.responses.create(
    model=deployment, input="...", max_output_tokens=1000, stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Structured output — JSON Schema

```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
```

## Tools (flat Responses format)

```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {"city_name": {"type": "string", "description": "The city name"}},
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

Tool call round-trip:
```python
import json
messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]
response = client.responses.create(model=deployment, input=messages, tools=tools, store=False)
tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    messages.extend(response.output)   # append the model's function_call items
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })
    response = client.responses.create(model=deployment, input=messages, tools=tools, store=False)
    print(response.output_text)
```

> `openai.pydantic_function_tool()` still generates the old nested format and is **not** compatible with `responses.create()`. Define tool schemas manually.

## Image input

Before (Chat): `{"type": "image_url", "image_url": {"url": "..."}}`
After (Responses): `{"type": "input_image", "image_url": "..."}` (flat string — HTTPS URL or `data:image/...;base64,...`). Also `{"type": "text"}` → `{"type": "input_text"}`.

```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {"type": "input_image", "image_url": "https://example.com/image.jpg"},
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

## Reasoning models (o1, o3, o3-mini, o4-mini, GPT-5 family)

| Chat Completions | Responses API | Notes |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Set high (4096+) |
| `reasoning_effort` | `reasoning={"effort": ...}` | keep low/medium/high |
| `temperature` | remove | GPT-5 rejects it outright (o-series only accepts `1`). To vary output, use a non-reasoning model such as `Llama-3.3-70B-Instruct` via Foundry Models. |
| `top_p` | remove | not supported |
| `seed` | remove | not supported |
