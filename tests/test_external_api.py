from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import get_exchange


@pytest.mark.parametrize("transaction", [{"operationAmount": {"amount": 555, "currency": {"code": "EUR"}}}])
@patch("requests.get")
def test_get_exchange(m_get: Any, transaction: Any) -> None:
    m_get.return_value = {"operationAmount": {"amount": 555, "currency": {"code": "EUR"}}}

    assert get_exchange(transaction) == 57847.71
