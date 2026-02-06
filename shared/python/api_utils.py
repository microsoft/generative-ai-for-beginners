"""
API utilities for safe HTTP requests and OpenAI client creation.

This module provides wrapper functions for making HTTP requests with
proper timeout, error handling, and retry logic.
"""

import os
from typing import Any, Optional

import requests
from requests.exceptions import RequestException


def make_safe_request(
    url: str,
    method: str = "GET",
    timeout: int = 30,
    retries: int = 3,
    **kwargs: Any
) -> requests.Response:
    """
    Make an HTTP request with proper timeout and error handling.

    Args:
        url: The URL to request.
        method: HTTP method (GET, POST, etc.).
        timeout: Request timeout in seconds.
        retries: Number of retry attempts.
        **kwargs: Additional arguments to pass to requests.

    Returns:
        The Response object.

    Raises:
        RequestException: If the request fails after all retries.

    Example:
        >>> response = make_safe_request("https://api.example.com/data")
        >>> data = response.json()
    """
    last_exception: Optional[Exception] = None

    for attempt in range(retries):
        try:
            response = requests.request(
                method=method,
                url=url,
                timeout=timeout,
                **kwargs
            )
            response.raise_for_status()
            return response
        except RequestException as e:
            last_exception = e
            if attempt < retries - 1:
                # Exponential backoff could be added here
                continue
            raise

    # This should never be reached, but just in case
    raise last_exception or RequestException("Request failed")


def create_openai_client(api_key: Optional[str] = None) -> Any:
    """
    Create an OpenAI client with proper configuration.

    Args:
        api_key: Optional API key. If not provided, reads from OPENAI_API_KEY env var.

    Returns:
        An OpenAI client instance.

    Raises:
        ValueError: If no API key is available.
        ImportError: If the openai package is not installed.

    Example:
        >>> client = create_openai_client()
        >>> response = client.chat.completions.create(...)
    """
    try:
        from openai import OpenAI
    except ImportError as e:
        raise ImportError(
            "The 'openai' package is required. Install it with: pip install openai"
        ) from e

    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError(
            "OpenAI API key is required. Set OPENAI_API_KEY environment variable "
            "or pass api_key parameter."
        )

    return OpenAI(api_key=key)


def create_azure_openai_client(
    endpoint: Optional[str] = None,
    api_key: Optional[str] = None,
    api_version: str = "2024-02-01"
) -> Any:
    """
    Create an Azure OpenAI client with proper configuration.

    Args:
        endpoint: Azure OpenAI endpoint URL. If not provided, reads from
                  AZURE_OPENAI_ENDPOINT env var.
        api_key: Azure OpenAI API key. If not provided, reads from
                 AZURE_OPENAI_API_KEY env var.
        api_version: Azure OpenAI API version.

    Returns:
        An AzureOpenAI client instance.

    Raises:
        ValueError: If endpoint or API key is missing.
        ImportError: If the openai package is not installed.

    Example:
        >>> client = create_azure_openai_client()
        >>> response = client.chat.completions.create(...)
    """
    try:
        from openai import AzureOpenAI
    except ImportError as e:
        raise ImportError(
            "The 'openai' package is required. Install it with: pip install openai"
        ) from e

    _endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
    _api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")

    if not _endpoint:
        raise ValueError(
            "Azure OpenAI endpoint is required. Set AZURE_OPENAI_ENDPOINT "
            "environment variable or pass endpoint parameter."
        )

    if not _api_key:
        raise ValueError(
            "Azure OpenAI API key is required. Set AZURE_OPENAI_API_KEY "
            "environment variable or pass api_key parameter."
        )

    return AzureOpenAI(
        azure_endpoint=_endpoint,
        api_key=_api_key,
        api_version=api_version
    )


def download_image(url: str, save_path: str, timeout: int = 30) -> str:
    """
    Download an image from a URL and save it to disk.

    Args:
        url: The URL of the image to download.
        save_path: The path where the image should be saved.
        timeout: Request timeout in seconds.

    Returns:
        The path where the image was saved.

    Raises:
        RequestException: If the download fails.
        IOError: If the file cannot be written.

    Example:
        >>> path = download_image("https://example.com/image.png", "./image.png")
    """
    response = make_safe_request(url, timeout=timeout)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(response.content)

    return save_path
