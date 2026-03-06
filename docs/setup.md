# Setup Guide

Welcome to **Generative AI for Beginners**! This guide walks you through configuring your development environment so you can run all course code samples.

---

## Prerequisites

| Requirement | Minimum version |
|---|---|
| Python | 3.10 |
| Node.js (optional, for TypeScript samples) | 18 LTS |
| Git | 2.x |

---

## 1. Clone the Repository

```bash
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners
```

## 2. Create and Activate a Virtual Environment

```bash
# Create the virtual environment
python -m venv .venv

# Activate on macOS / Linux
source .venv/bin/activate

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## 3. Install Python Dependencies

Each lesson folder contains its own `requirements.txt`. Install globally for all lessons:

```bash
pip install -r requirements.txt
```

Or navigate into a specific lesson directory and install only what that lesson needs:

```bash
cd 06-text-generation-apps
pip install -r requirements.txt
```

## 4. Configure Your LLM Provider

The course supports three providers. Choose one and follow the corresponding instructions.

### Option A – Azure OpenAI Service

1. Create an [Azure OpenAI resource](https://aka.ms/genai-beginners/azure-open-ai).
2. Deploy a model (e.g., `gpt-4o`).
3. Copy `.env.copy` to `.env` inside the lesson folder and fill in the values:

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-deployment-name>
AZURE_OPENAI_API_VERSION=2024-02-01
```

### Option B – GitHub Marketplace Models

1. Generate a [GitHub personal access token](https://github.com/settings/tokens) with `models:read` scope.
2. Add the token to `.env`:

```env
GITHUB_TOKEN=<your-github-token>
```

### Option C – OpenAI API

1. Create an account at <https://platform.openai.com>.
2. Generate an API key.
3. Add it to `.env`:

```env
OPENAI_API_KEY=<your-api-key>
```

## 5. (Optional) Install Node.js Dependencies

For TypeScript samples, install dependencies inside the lesson folder:

```bash
cd 06-text-generation-apps
npm install
```

## 6. Run the Starter Script

From the repository root, verify your setup by running:

```bash
python src/main.py
```

## 7. Run the Tests

```bash
pytest tests/
```

---

## Project Structure

```
generative-ai-for-beginners/
├── src/
│   └── main.py          # Starter entry-point script
├── docs/
│   └── setup.md         # This file – environment setup guide
├── tests/
│   └── test_main.py     # Placeholder unit tests
├── 00-course-setup/     # Lesson 0: development environment guide
├── 01-introduction-to-genai/
│   └── ...              # Lessons 1-21 follow the same pattern
├── .env.copy            # Template for environment variables
├── .gitignore
└── README.md
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError` when importing `openai` | Activate the virtual environment and run `pip install -r requirements.txt` |
| `AuthenticationError` from the API | Double-check the API key in your `.env` file |
| `pytest: command not found` | Install pytest: `pip install pytest` |

---

For further help, join the [Azure AI Foundry Discord](https://aka.ms/genai-discord) or open an issue on GitHub.
