import pytest

import pytest


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Список словарей с разными state и датами — базовые данные для processing."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-15T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-05-20T08:30:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2023-12-31T23:59:59.999999"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},  # дубль даты
        {"id": 6, "state": "CANCELED", "date": "2024-06-01T12:00:00.000000"},
    ]


@pytest.fixture
def empty_transactions() -> list[dict]:
    """Пустой список — граничный случай."""
    return []


@pytest.fixture
def no_state_transactions() -> list[dict]:
    """Список без словарей с нужным статусом."""
    return [
        {"id": 1, "state": "CANCELED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "PENDING", "date": "2024-01-15T10:00:00.000000"},
    ]


@pytest.fixture
def sample_dates() -> list[dict]:
    """Разные форматы дат для сортировки."""
    return [
        {"id": 1, "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "date": "2023-01-01T00:00:00.000000"},
        {"id": 3, "date": "2024-12-31T23:59:59.999999"},
    ]