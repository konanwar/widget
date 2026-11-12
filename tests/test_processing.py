import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:

    def test_filter_executed(self, sample_transactions: list[dict]) -> None:
        result = filter_by_state(sample_transactions, state="EXECUTED")
        assert all(item["state"] == "EXECUTED" for item in result)
        assert {item["id"] for item in result} == {1, 3, 5}

    def test_filter_canceled(self, sample_transactions: list[dict]) -> None:
        result = filter_by_state(sample_transactions, state="CANCELED")
        assert {item["id"] for item in result} == {2, 6}

    def test_default_state(self, sample_transactions: list[dict]) -> None:
        """Без явного аргумента state фильтрует по EXECUTED."""
        assert filter_by_state(sample_transactions) == filter_by_state(
            sample_transactions, state="EXECUTED"
        )

    def test_no_matching_state(self, no_state_transactions: list[dict]) -> None:
        """Статуса нет ни у одного словаря — пустой список, а не ошибка."""
        assert filter_by_state(no_state_transactions, state="EXECUTED") == []

    def test_empty_list(self, empty_transactions: list[dict]) -> None:
        assert filter_by_state(empty_transactions) == []

    @pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", "PENDING", "UNKNOWN"])
    def test_parametrized_states(self, sample_transactions: list[dict], state: str) -> None:
        result = filter_by_state(sample_transactions, state=state)
        if state != "UNKNOWN":
            assert all(item["state"] == state for item in result)
        else:
            assert result == []


class TestSortByDate:

    def test_sort_descending_default(self, sample_transactions: list[dict]) -> None:
        result = sort_by_date(sample_transactions)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=True)
        assert result[0]["id"] == 6  # самая свежая дата

    def test_sort_ascending(self, sample_transactions: list[dict]) -> None:
        result = sort_by_date(sample_transactions, reverse=False)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates)
        assert result[0]["id"] == 4  # самая старая

    def test_same_dates_keep_stable(self, sample_transactions: dict) -> None:
        """При одинаковых датах исходный порядок не ломается."""
        result = sort_by_date(sample_transactions)
        ids_same_date = [i["id"] for i in result if i["date"] == "2024-03-11T02:26:18.671407"]
        assert ids_same_date == [6, 1, 3] or ids_same_date[:2] == sorted(ids_same_date[:2])

    def test_empty_list(self, empty_transactions: list[dict]) -> None:
        assert sort_by_date(empty_transactions) == []

    @pytest.mark.parametrize(
        "wrong_item",
        [{"id": 1, "date": "не дата"}, {"id": 1}, "строка вместо словаря"],
    )
    def test_invalid_date_formats(self, wrong_item) -> None:
        """Некорректная дата/структура — ожидаем ошибку."""
        with pytest.raises((ValueError, TypeError, KeyError)):
            sort_by_date([wrong_item])