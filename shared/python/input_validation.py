"""
Input validation utilities for secure user input handling.

This module provides functions to validate and sanitize user input,
protecting against prompt injection and other input-based attacks.
"""

import re
from typing import Optional


def validate_number_input(
    value: str,
    min_val: int = 1,
    max_val: int = 100,
    field_name: str = "number"
) -> int:
    """
    Validate and convert string input to an integer within bounds.

    Args:
        value: The string value to validate.
        min_val: Minimum allowed value (inclusive).
        max_val: Maximum allowed value (inclusive).
        field_name: Name of the field for error messages.

    Returns:
        The validated integer value.

    Raises:
        ValueError: If the value is not a valid integer or is out of bounds.

    Example:
        >>> num = validate_number_input("5", min_val=1, max_val=20)
        >>> print(num)  # 5
    """
    try:
        num = int(value.strip())
        if num < min_val or num > max_val:
            raise ValueError(
                f"{field_name} must be between {min_val} and {max_val}, got {num}"
            )
        return num
    except (ValueError, AttributeError) as e:
        if "must be between" in str(e):
            raise
        raise ValueError(
            f"Please enter a valid {field_name} between {min_val} and {max_val}"
        ) from e


def validate_text_input(
    value: str,
    max_length: int = 500,
    min_length: int = 1,
    allow_empty: bool = False,
    field_name: str = "input"
) -> str:
    """
    Validate and sanitize text input.

    Args:
        value: The string value to validate.
        max_length: Maximum allowed length.
        min_length: Minimum required length.
        allow_empty: Whether to allow empty strings.
        field_name: Name of the field for error messages.

    Returns:
        The validated and trimmed string.

    Raises:
        ValueError: If the value fails validation.

    Example:
        >>> text = validate_text_input("Hello World", max_length=100)
    """
    if value is None:
        if allow_empty:
            return ""
        raise ValueError(f"{field_name} cannot be None")

    trimmed = value.strip()

    if not trimmed and not allow_empty:
        raise ValueError(f"{field_name} cannot be empty")

    if len(trimmed) > max_length:
        raise ValueError(
            f"{field_name} is too long. Maximum {max_length} characters allowed, "
            f"got {len(trimmed)}"
        )

    if len(trimmed) < min_length:
        raise ValueError(
            f"{field_name} is too short. Minimum {min_length} characters required"
        )

    return trimmed


def sanitize_prompt_input(
    value: str,
    max_length: int = 1000,
    strict: bool = False
) -> str:
    """
    Sanitize user input intended for use in LLM prompts.

    This function removes potentially dangerous characters and patterns
    that could be used for prompt injection attacks.

    Args:
        value: The string to sanitize.
        max_length: Maximum allowed length after sanitization.
        strict: If True, only allow alphanumeric, spaces, and basic punctuation.

    Returns:
        The sanitized string.

    Raises:
        ValueError: If the input is too long or contains only invalid characters.

    Example:
        >>> safe_input = sanitize_prompt_input("Hello, world!")
    """
    if not value:
        return ""

    # Trim whitespace
    sanitized = value.strip()

    # Remove null bytes and control characters (except newlines and tabs)
    sanitized = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', sanitized)

    # Remove potentially dangerous template/injection patterns
    dangerous_patterns = [
        r'\{\{.*?\}\}',  # Template injection
        r'\${.*?}',      # Variable substitution
        r'<script.*?>.*?</script>',  # Script tags
        r'javascript:',  # JavaScript URLs
    ]

    for pattern in dangerous_patterns:
        sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE | re.DOTALL)

    if strict:
        # In strict mode, only allow safe characters
        sanitized = re.sub(r'[^\w\s,.\'\"-?!@#$%&*()+=:;]', '', sanitized, flags=re.UNICODE)

    # Normalize whitespace
    sanitized = re.sub(r'\s+', ' ', sanitized)
    sanitized = sanitized.strip()

    if len(sanitized) > max_length:
        raise ValueError(f"Input too long. Maximum {max_length} characters allowed.")

    if not sanitized:
        raise ValueError("Input contains only invalid characters")

    return sanitized


def validate_email(email: str) -> str:
    """
    Validate an email address format.

    Args:
        email: The email address to validate.

    Returns:
        The validated email address (lowercase).

    Raises:
        ValueError: If the email format is invalid.
    """
    email = email.strip().lower()

    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(pattern, email):
        raise ValueError(f"Invalid email format: {email}")

    return email


def validate_url(url: str, require_https: bool = True) -> str:
    """
    Validate a URL format.

    Args:
        url: The URL to validate.
        require_https: If True, only allow HTTPS URLs.

    Returns:
        The validated URL.

    Raises:
        ValueError: If the URL format is invalid.
    """
    url = url.strip()

    # Basic URL pattern
    if require_https:
        pattern = r'^https://[a-zA-Z0-9.-]+(?:/[^\s]*)?$'
        if not re.match(pattern, url):
            raise ValueError(f"Invalid HTTPS URL: {url}")
    else:
        pattern = r'^https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?$'
        if not re.match(pattern, url):
            raise ValueError(f"Invalid URL: {url}")

    return url
