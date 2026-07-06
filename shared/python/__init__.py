"""
Shared utilities for the Generative AI for Beginners course.

This module provides common functionality used across multiple lessons,
including environment variable handling, input validation, and API utilities.
"""

from .api_utils import (
    create_azure_openai_client,
    create_openai_client,
    make_safe_request,
)
from .env_utils import get_required_env, validate_env_vars
from .input_validation import (
    sanitize_prompt_input,
    validate_number_input,
    validate_text_input,
)

__all__ = [
    "get_required_env",
    "validate_env_vars",
    "validate_number_input",
    "validate_text_input",
    "sanitize_prompt_input",
    "make_safe_request",
    "create_openai_client",
    "create_azure_openai_client",
]
