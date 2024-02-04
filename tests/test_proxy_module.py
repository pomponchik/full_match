import re

import pytest

import full_match


def test_simple_match():
    assert re.search(full_match('kek'), 'XXkekXX') is None
    assert re.search(full_match('kek'), '++kek++') is None


@pytest.mark.parametrize(
    'addictional_string', [
        'XX',
        'XXX',
        'kek',
        'ogogo',
    ],
)
def test_exception_message(addictional_string):
    with pytest.raises(AssertionError, match='Regex pattern did not match.'):
        with pytest.raises(ValueError, match=full_match('kek')):
            raise ValueError(f'{addictional_string}kek{addictional_string}')
