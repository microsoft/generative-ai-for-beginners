from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the GITHUB_TOKEN variable
# github_token = os.getenv("GITHUB_TOKEN")

# Print the environment variables
print("Environment Variables:")
print("   GITHUB_TOKEN:", os.getenv("GITHUB_TOKEN"))
print("    GITHUB_REPO:", os.getenv("GITHUB_REPO"))
print("GITHUB_USERNAME:", os.getenv("GITHUB_USERNAME"))
