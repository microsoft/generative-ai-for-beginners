---
name: azure-openai-to-responses
description: >-
  Migrate Python apps from Azure OpenAI Chat Completions to the Responses API.
  Covers AzureOpenAI/AsyncAzureOpenAI client migration to the v1 endpoint,
  streaming, tools, structured output, multi-turn, EntraID auth, and model
  compatibility checks. Python-focused, Azure OpenAI-specific.
  USE FOR: migrate to responses API, switch from chat completions, openai responses,
  upgrade openai SDK, responses API migration, move from completions to responses,
  gpt-5 migration, azure openai python migration, chat completions to responses,
  AzureOpenAI to OpenAI client, python azure openai upgrade.
  DO NOT USE FOR: building new apps from scratch (start with responses directly),
  Node/TypeScript/C#/Java/Go migrations (this skill is Python-only),
  Azure infrastructure setup (use azure-prepare), deploying models (use microsoft-foundry).
license: MIT
source: https://github.com/Azure-Samples/azure-openai-to-responses
---

# Migrate Python Apps from Azure OpenAI Chat Completions to Responses API

> **AUTHORITATIVE GUIDANCE — FOLLOW EXACTLY**
>
> This skill migrates Python codebases using Azure OpenAI Chat Completions
> to the unified Responses API. Follow these instructions precisely.
> Do not improvise parameter mappings or invent API shapes.

Installed from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) (MIT).

## Triggers

Activate this skill when the user wants to:
- Migrate a Python app from Azure OpenAI Chat Completions to Responses API
- Upgrade Python OpenAI SDK usage to the latest API shape against Azure OpenAI
- Prepare Python code for GPT-5 or newer models that require Responses on Azure
- Switch from `AzureOpenAI`/`AsyncAzureOpenAI` to standard `OpenAI`/`AsyncOpenAI` client with the v1 endpoint
- Fix deprecation warnings related to `AzureOpenAI` constructors or `api_version`

## Why migrate

GPT-5 and newer models require the Responses API. The new `/openai/v1/` endpoint
uses the standard `OpenAI()` client instead of `AzureOpenAI()`, requires no
`api_version` parameter, and works identically across OpenAI and Azure OpenAI.

## What changes

| Chat Completions (before) | Responses API (after) |
| --- | --- |
| `AzureOpenAI()` / `AsyncAzureOpenAI()` | `OpenAI(base_url=...)` / `AsyncOpenAI(base_url=...)` |
| `azure_endpoint=...` | `base_url=f"{endpoint.rstrip('/')}/openai/v1/"` |
| `api_version="2024-..."` | Remove entirely — `/openai/v1/` is stable |
| `azure_ad_token_provider=...` | `api_key=token_provider` |
| `client.chat.completions.create(messages=...)` | `client.responses.create(input=...)` |
| `resp.choices[0].message.content` | `resp.output_text` |
| `max_tokens` | `max_output_tokens` (min 16 on Azure) |
| `response_format` | `text={"format": {...}}` |
| `seed` | **Remove** (not supported) |
| tools nested `{"type":"function","function":{...}}` | flat `{"type":"function","name":...}` |
| tool result `{"role":"tool","tool_call_id":...}` | `{"type":"function_call_output","call_id":...,"output":...}` |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` + `{"url": "..."}` | `content[].type: "input_image"` + flat `"image_url": "..."` |
| streaming `chunk.choices[0].delta.content` | `event.type == "response.output_text.delta"` → `event.delta` |

## Model compatibility — CHECK FIRST

Verify the deployed model supports the Responses API before migrating. GPT-4o and
GPT-4 support Responses for basic text/chat/streaming/tools but not all features.
Newer models (gpt-4.1+, gpt-5.x) have full support. **GitHub Models
(`models.github.ai`, `models.inference.ai.azure.com`) do NOT support the Responses
API** — remove those code paths and switch to Azure OpenAI, OpenAI, or a compatible
local endpoint.

Smoke test:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
resp = client.responses.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    input="ping",
    max_output_tokens=50,
    store=False,
)
print(resp.output_text)
```

## Step 0: Client migration (prerequisite)

`AzureOpenAI`/`AsyncAzureOpenAI` constructors are deprecated in `openai>=1.108.1`.

Before:
```python
from openai import AzureOpenAI
client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
```

After:
```python
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Cleanup: remove `api_version` args, remove `AZURE_OPENAI_API_VERSION` /
`AZURE_OPENAI_VERSION` from `.env`/infra, rename `AZURE_OPENAI_CLIENT_ID` →
`AZURE_CLIENT_ID`, ensure `openai>=1.108.1`.

## Step 1: Detect legacy call sites

```bash
rg "chat\.completions\.create"        # legacy API calls
rg "ChatCompletion\.create|Completion\.create"
rg "AzureOpenAI\(|AsyncAzureOpenAI\("  # deprecated constructors
rg "choices\[0\]\.message\.content"    # response access
rg "choices\[0\]\.delta\.content"      # streaming access
rg "max_tokens\b"                      # rename to max_output_tokens
rg "['\"]seed['\"]"                    # remove entirely
rg "response_format"                   # → text.format
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "models\.github\.ai|models\.inference\.ai\.azure"  # GitHub Models: remove
```

## Step 2: Apply migration

- `client.chat.completions.create(messages=...)` → `client.responses.create(input=...)`
- `resp.choices[0].message.content` → `resp.output_text`
- `max_tokens` → `max_output_tokens` (min 16); remove `seed`
- `response_format` → `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`
- Set `store=False` on every request (client-managed state)
- Streaming: iterate events, handle `event.type == "response.output_text.delta"` (use `event.delta`) and `response.completed`
- Tools: flat format, `tool_choice`, return results as `function_call_output` items; append `response.output` items for round-trips
- Multi-turn: maintain conversation in an `input` array, or use `previous_response_id` (requires `store=True`)
- Reasoning models (o-series, GPT-5): `max_completion_tokens` → `max_output_tokens` (4096+), `reasoning_effort` → `reasoning={"effort": ...}`, omit `temperature`/`top_p` (GPT-5 rejects `temperature` outright; to vary output use a non-reasoning model like `Llama-3.3-70B-Instruct` via Foundry Models)

## Acceptance criteria (all must pass)

- Zero matches for `chat.completions.create|ChatCompletion.create|Completion.create`
- Zero matches for `AzureOpenAI(|AsyncAzureOpenAI(` — all use `OpenAI`/`AsyncOpenAI` + v1 endpoint
- Zero matches for `models.github.ai|models.inference.ai.azure`
- Zero matches for `choices[0]` — all access uses `resp.output_text` / Responses schema
- No top-level `response_format`; structured output uses `text={"format": {...}}`
- `openai>=1.108.1` in requirements; `store=False` on every call; no `api_version` in client construction
- Tests updated (mocks use `kwargs.get("input")`, snapshots use Responses shape); `pytest` passes

See [references/cheat-sheet.md](./references/cheat-sheet.md) for complete before/after code examples.

## References

- [Azure OpenAI Responses API docs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/responses)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)
- [Source skill: Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)
