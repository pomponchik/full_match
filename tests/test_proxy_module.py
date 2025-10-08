import re

import pytest

from full_match import match


def test_simple_match():
    assert re.search(match('kek'), 'XXkekXX') is None
    assert re.search(match('kek'), '++kek++') is None


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
        with pytest.raises(ValueError, match=match('kek')):
            raise ValueError(f'{addictional_string}kek{addictional_string}')


def test_exception_message_like_in_readme():
  with pytest.raises(AssertionError, match='Regex pattern did not match.'):
    with pytest.raises(ValueError, match=match('Some message.')):
      raise ValueError('XXSome message.XX')
