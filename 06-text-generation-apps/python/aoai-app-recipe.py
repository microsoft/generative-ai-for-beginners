from openai import OpenAI
import os
import re
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# SECURITY: Validate environment variables with helpful error messages
def get_required_env(var_name: str) -> str:
    """Get a required environment variable or raise an error with helpful message."""
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Missing required environment variable: {var_name}. Please set it in your .env file.")
    return value

# SECURITY: Input validation functions
def validate_number_input(value: str, min_val: int = 1, max_val: int = 20) -> int:
    """Validate and sanitize numeric input."""
    try:
        num = int(value)
        if num < min_val or num > max_val:
            raise ValueError(f"Number must be between {min_val} and {max_val}")
        return num
    except ValueError:
        raise ValueError(f"Please enter a valid number between {min_val} and {max_val}")

def validate_text_input(value: str, max_length: int = 500) -> str:
    """Validate and sanitize text input to prevent prompt injection."""
    if len(value) > max_length:
        raise ValueError(f"Input too long. Maximum {max_length} characters allowed.")
    # Remove potentially dangerous characters/patterns
    sanitized = re.sub(r'[<>{}[\]|\\`]', '', value)
    # Limit to alphanumeric, spaces, commas, and basic punctuation
    if not re.match(r'^[\w\s,.\'-]+$', sanitized, re.UNICODE):
        raise ValueError("Input contains invalid characters")
    return sanitized.strip()

# configure the OpenAI client against the Azure OpenAI (Microsoft Foundry) v1 endpoint
client = OpenAI(
    api_key=get_required_env('AZURE_OPENAI_API_KEY'),
    base_url=f"{get_required_env('AZURE_OPENAI_ENDPOINT').rstrip('/')}/openai/v1/",
)

deployment = get_required_env('AZURE_OPENAI_DEPLOYMENT')

# SECURITY: Validate all user inputs
try:
    no_recipes_input = input("No of recipes (for example, 5): ")
    no_recipes = validate_number_input(no_recipes_input, 1, 20)

    ingredients_input = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
    ingredients = validate_text_input(ingredients_input, 500)

    filter_input = input("Filter (for example, vegetarian, vegan, or gluten-free): ")
    filter_value = validate_text_input(filter_input, 100) if filter_input.strip() else "none"
except ValueError as e:
    print(f"Input validation error: {e}")
    exit(1)

# interpolate the number of recipes into the prompt and ingredients
# Note: Using validated and sanitized inputs
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter_value}: "

response = client.responses.create(model=deployment, input=prompt, max_output_tokens=600, store=False)


# print response
print("Recipes:")
old_prompt_result = response.output_text
if not old_prompt_result:
    print("No response received.")
else:
    print(old_prompt_result)

    prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "
    new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
    response = client.responses.create(model=deployment, input=new_prompt, max_output_tokens=600, store=False)

    # print response
    print("\n=====Shopping list ======= \n")
    if response.output_text:
        print(response.output_text)
    else:
        print("No response received.")

