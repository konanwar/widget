import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_number, expected', [('7000792289606361','7000 79** **** 6361')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize('account, expected',[('73654108430135874305','**4305')])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected