import pytest

from typing import Any

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты маскирования номера карты."""

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("9999999999999999", "9999 99** **** 9999"),
        ],
    )
    def test_valid_card_numbers(self, card_number: str, expected: str) -> None:
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000 7922 8960 6361", "7000 79** **** 6361"),  # с пробелами
            ("7000-7922-8960-6361", "7000 79** **** 6361"),  # с дефисами
            (" 7000792289606361 ", "7000 79** **** 6361"),   # с лишними пробелами
        ],
    )
    def test_nonstandard_formats(self, card_number: str, expected: str) -> None:
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "wrong_input",
        ["", "1234", "123456789012", "12345678901234567890", "abcd12345678efgh", None],
    )
    def test_invalid_input(self, wrong_input: Any) -> None:
        """Некорректная длина или нецифровые символы — ожидаем ошибку."""
        with pytest.raises((ValueError, TypeError)):
            get_mask_card_number(wrong_input)


class TestGetMaskAccount:
    """Тесты маскирования номера счёта."""

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("00000000000000000000", "**0000"),
            ("99999999999999999999", "**9999"),
        ],
    )
    def test_valid_account_numbers(self, account_number: str, expected: str) -> None:
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "wrong_input",
        ["", "1234", "12345678", "736541084301358743051", "abcdefghij", None],
    )
    def test_short_or_invalid_input(self, wrong_input: Any) -> None:
        """Номер счёта короче/длиннее 20 цифр или нецифровой — ошибка."""
        with pytest.raises((ValueError, TypeError)):
            get_mask_account(wrong_input)