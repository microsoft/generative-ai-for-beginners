"""Tests for shared.python.env_utils."""

import pytest

from shared.python.env_utils import (
    get_env_with_default,
    get_required_env,
    validate_env_vars,
)


def test_get_required_env_returns_value(monkeypatch):
    monkeypatch.setenv("MY_VAR", "hello")
    assert get_required_env("MY_VAR") == "hello"


def test_get_required_env_missing_raises(monkeypatch):
    monkeypatch.delenv("MISSING_VAR", raising=False)
    with pytest.raises(ValueError, match="MISSING_VAR"):
        get_required_env("MISSING_VAR")


def test_get_required_env_empty_raises(monkeypatch):
    monkeypatch.setenv("EMPTY_VAR", "")
    with pytest.raises(ValueError):
        get_required_env("EMPTY_VAR")


def test_get_required_env_includes_description(monkeypatch):
    monkeypatch.delenv("NEEDS_DESC", raising=False)
    with pytest.raises(ValueError, match="OpenAI authentication"):
        get_required_env("NEEDS_DESC", "OpenAI authentication")


def test_validate_env_vars_returns_mapping(monkeypatch):
    monkeypatch.setenv("VAR_A", "1")
    monkeypatch.setenv("VAR_B", "2")
    result = validate_env_vars("VAR_A", "VAR_B")
    assert result == {"VAR_A": "1", "VAR_B": "2"}


def test_validate_env_vars_reports_all_missing(monkeypatch):
    monkeypatch.delenv("VAR_X", raising=False)
    monkeypatch.delenv("VAR_Y", raising=False)
    with pytest.raises(ValueError) as exc_info:
        validate_env_vars("VAR_X", "VAR_Y")
    message = str(exc_info.value)
    assert "VAR_X" in message
    assert "VAR_Y" in message


def test_get_env_with_default_uses_default(monkeypatch):
    monkeypatch.delenv("UNSET_VAR", raising=False)
    assert get_env_with_default("UNSET_VAR", "fallback") == "fallback"


def test_get_env_with_default_uses_value(monkeypatch):
    monkeypatch.setenv("SET_VAR", "actual")
    assert get_env_with_default("SET_VAR", "fallback") == "actual"
