"""
test_main.py - Placeholder tests for src/main.py.

Run with:  pytest tests/
"""

import pytest

from src.main import get_greeting


class TestGetGreeting:
    """Tests for the get_greeting helper function."""

    def test_returns_string(self):
        result = get_greeting("Alice")
        assert isinstance(result, str)

    def test_contains_name(self):
        result = get_greeting("Alice")
        assert "Alice" in result

    def test_greeting_for_different_names(self):
        for name in ["Bob", "Charlie", "Generative AI"]:
            result = get_greeting(name)
            assert name in result, f"Expected '{name}' to appear in greeting"

    def test_empty_name(self):
        # Edge-case: empty string should still return a string without raising.
        result = get_greeting("")
        assert isinstance(result, str)
