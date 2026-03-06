"""
main.py - Entry point for the Generative AI for Beginners project.

This starter module demonstrates how to interact with a language model API.
Replace the placeholder logic below with your own implementation.
"""


def get_greeting(name: str) -> str:
    """Return a personalised greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Welcome to Generative AI for Beginners."


def main() -> None:
    """Run the main application logic."""
    # TODO: Configure your preferred LLM provider here.
    # Supported options: Azure OpenAI, GitHub Models, OpenAI API.
    # See docs/setup.md for detailed configuration instructions.

    user_name = input("Enter your name: ")
    print(get_greeting(user_name))
    print("\nNext steps:")
    print("  1. Read docs/setup.md to configure your environment.")
    print("  2. Explore the lesson directories (01-introduction-to-genai, etc.).")
    print("  3. Run the lesson code samples to see Generative AI in action.")


if __name__ == "__main__":
    main()
