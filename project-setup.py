from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the GITHUB_TOKEN variable
github_token = os.getenv("GITHUB_TOKEN")

print(github_token)
