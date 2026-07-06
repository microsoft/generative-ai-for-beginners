#!/bin/bash

# Install OpenAI and Dotenv for Python
# TODO: Check why this can't be done in requirements.txt
pip install python-dotenv
pip install openai

# Install developer tooling for linting, formatting, type-checking, and tests.
# These match the checks run in .github/workflows/code-quality.yml so
# contributors can reproduce them locally before opening a pull request.
pip install ruff black mypy pytest

# Install the OpenAI packages for Node.js
# (Python related dependencies are covered in requirements.txt)
# echo "Installing OpenAI For Node.js" 
# npm install --save openai
