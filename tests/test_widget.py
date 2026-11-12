from typing import Any

import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты универсального маскирования «тип + номер»."""

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 5100123412341234", "MasterCard 5100 12** **** 1234"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счёт 73654108430135874305", "Счёт **4305"),
            ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ],
    )
    def test_card_and_account(self, input_str: str, expected: str) -> None:
        assert mask_account_card(input_str) == expected

    def test_recognition_by_type(self) -> None:
        """20-значный номер маскируется как счёт, 16-значный — как карта."""
        assert mask_account_card("Счет 73654108430135874305").startswith("Счет **")
        assert mask_account_card("Visa 7000792289606361").endswith("6361")

    @pytest.mark.parametrize(
        "wrong_input",
        ["", "Visa", "Счет 12345", "7000792289606361", None],
    )
    def test_invalid_input(self, wrong_input: Any) -> None:
        """Без типа или без номера — ожидаем ошибку."""
        with pytest.raises((ValueError, TypeError)):
            mask_account_card(wrong_input)


class TestGetDate:
    """Тесты преобразования даты."""

    @pytest.mark.parametrize(
        "input_date, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2024-01-01T00:00:00", "01.01.2024"),
            ("2023-12-31T23:59:59.999999", "31.12.2023"),
            ("2000-02-29T12:00:00", "29.02.2000"),  # високосный год
        ],
    )
    def test_valid_dates(self, input_date: str, expected: str) -> None:
        assert get_date(input_date) == expected

    @pytest.mark.parametrize(
        "wrong_input",
        ["", "не дата", "11.03.2024", None],
    )
    def test_invalid_dates(self, wrong_input: Any) -> None:
        with pytest.raises((ValueError, TypeError)):
            get_date(wrong_input)