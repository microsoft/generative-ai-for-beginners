"""Tests for shared.python.api_utils."""

import pytest
from requests.exceptions import RequestException

from shared.python.api_utils import (
    create_azure_openai_client,
    create_openai_client,
    make_safe_request,
)


class _FakeResponse:
    def __init__(self):
        self.raised = False

    def raise_for_status(self):
        self.raised = True


class TestMakeSafeRequest:
    def test_returns_response_on_success(self, monkeypatch):
        fake = _FakeResponse()

        def fake_request(method, url, timeout, **kwargs):
            assert timeout == 30
            return fake

        monkeypatch.setattr("shared.python.api_utils.requests.request", fake_request)
        result = make_safe_request("https://example.com")
        assert result is fake
        assert fake.raised is True

    def test_retries_then_raises(self, monkeypatch):
        calls = {"count": 0}

        def fake_request(method, url, timeout, **kwargs):
            calls["count"] += 1
            raise RequestException("boom")

        monkeypatch.setattr("shared.python.api_utils.requests.request", fake_request)
        with pytest.raises(RequestException):
            make_safe_request("https://example.com", retries=3)
        assert calls["count"] == 3


class TestCreateOpenAIClient:
    def test_missing_key_raises_value_error(self, monkeypatch):
        pytest.importorskip("openai")
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        with pytest.raises(ValueError, match="API key"):
            create_openai_client()


class TestCreateAzureOpenAIClient:
    def test_missing_endpoint_raises_value_error(self, monkeypatch):
        pytest.importorskip("openai")
        monkeypatch.delenv("AZURE_OPENAI_ENDPOINT", raising=False)
        monkeypatch.setenv("AZURE_OPENAI_API_KEY", "test-key")
        with pytest.raises(ValueError, match="endpoint"):
            create_azure_openai_client()

    def test_missing_key_raises_value_error(self, monkeypatch):
        pytest.importorskip("openai")
        monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com")
        monkeypatch.delenv("AZURE_OPENAI_API_KEY", raising=False)
        with pytest.raises(ValueError, match="API key"):
            create_azure_openai_client()
