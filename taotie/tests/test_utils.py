"""Test the utils.
Run this test with command: pytest taotie/tests/test_utils.py
"""
from unittest.mock import patch

import pytest

from taotie.utils import *


@pytest.mark.parametrize(
    "input, expected",
    [(1681684094, "2023-04-16 14:28:14")],
)
def test_get_datetime(input, expected):
    assert get_datetime(input) == expected


@pytest.mark.parametrize(
    "url, response_text, status_code, expected_output, expected_exception",
    [
        (
            "https://raw.githubusercontent.com/Open-EdTech/python-for-dev/main/README.md",
            "Python for Developers",
            200,
            "Python for Developers",
            None,
        ),  # Test with a valid URL
        (
            "https://example.com/404",
            "",
            404,
            None,
            Exception,
        ),  # Test with a 404 error
        (
            "https://example.com/notfound",
            "",
            500,
            None,
            Exception,
        ),  # Test with a 500 error
    ],
)
def test_fetch_url_content(
    url, response_text, status_code, expected_output, expected_exception
):
    with patch("requests.get") as mock_get:
        mock_get.return_value.text = response_text
        mock_get.return_value.status_code = status_code

        if expected_exception:
            with pytest.raises(expected_exception):
                fetch_url_content(url)
        else:
            assert fetch_url_content(url) == expected_output
