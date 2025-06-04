from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Access the GitHub token
github_token = os.getenv("GITHUB_TOKEN")

print(github_token)
