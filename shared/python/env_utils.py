"""
Environment variable utilities for secure configuration management.

This module provides functions to safely retrieve and validate environment
variables, ensuring that sensitive configuration is properly handled.
"""

import os
from typing import Optional


def get_required_env(var_name: str, description: Optional[str] = None) -> str:
    """
    Get a required environment variable or raise an error with helpful message.

    Args:
        var_name: The name of the environment variable to retrieve.
        description: Optional description of what the variable is used for.

    Returns:
        The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set or is empty.

    Example:
        >>> api_key = get_required_env("OPENAI_API_KEY", "OpenAI API authentication")
    """
    value = os.getenv(var_name)
    if not value:
        desc_part = f" ({description})" if description else ""
        raise ValueError(
            f"Missing required environment variable: {var_name}{desc_part}. "
            f"Please set it in your .env file or environment."
        )
    return value


def validate_env_vars(*var_names: str) -> dict[str, str]:
    """
    Validate that multiple environment variables are set.

    Args:
        *var_names: Variable names to check.

    Returns:
        Dictionary mapping variable names to their values.

    Raises:
        ValueError: If any of the required variables are missing.

    Example:
        >>> env = validate_env_vars("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY")
        >>> print(env["AZURE_OPENAI_ENDPOINT"])
    """
    missing = []
    values = {}

    for var_name in var_names:
        value = os.getenv(var_name)
        if not value:
            missing.append(var_name)
        else:
            values[var_name] = value

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}. "
            f"Please set them in your .env file or environment."
        )

    return values


def get_env_with_default(var_name: str, default: str) -> str:
    """
    Get an environment variable with a default value.

    Args:
        var_name: The name of the environment variable.
        default: The default value if the variable is not set.

    Returns:
        The value of the environment variable or the default.

    Example:
        >>> model = get_env_with_default("MODEL_NAME", "gpt-4o")
    """
    return os.getenv(var_name, default)
