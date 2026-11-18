import pytest

@pytest.fixture
def for_test_generators() -> list[dict]:
    """список словарей с раздичными валютами"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]



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