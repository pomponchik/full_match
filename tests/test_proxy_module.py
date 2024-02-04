import re

import pytest

import full_match


def test_simple_match():
    assert re.search(full_match('kek'), 'XXkekXX') is None


def test_exception_message():
    with pytest.raises(AssertionError, match='Regex pattern did not match.'):
        with pytest.raises(ValueError, match=full_match('kek')):
            raise ValueError('XXkekXX')
