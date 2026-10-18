from src.widget import mask_account_card


def test_mask_account_card():
     assert mask_account_card ("7000792289606361") == '7000 79** **** 6361'
