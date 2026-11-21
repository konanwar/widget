from typing import Iterable, Any

from collections.abc import Iterator


def filter_by_currency(records: Iterable[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]:
    """поочередно выдает транзакции по коду валюты """
    if not isinstance(records, list):
        raise TypeError("Ожидается список словарей")

    for record in records:
        operation_amount = record.get("operationAmount", {})
        valid_corr = operation_amount.get("currency", {})
        code = valid_corr.get('code') or ''
        if code.upper() == currency.upper():
            yield record


def transaction_descriptions(records: list[dict]) -> Iterator[str]:
    """возвращает описание каждой операции по очереди"""
    if not isinstance(records, list):
        raise TypeError("Ожидается список словарей")

    for record in records:
        description = record.get('description')
        if description is not None:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if not isinstance(start, int) or isinstance(start, bool) \
            or not isinstance(stop, int) or isinstance(stop, bool):
        raise TypeError("Начало и конец диапазона должны быть целыми числами")
    if start < 1 or stop > 9999999999999999:
        raise ValueError("Диапазон номеров карт: от 1 до 9999999999999999")
    if start > stop:
        raise ValueError("Начальное значение не может быть больше конечного")

    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " \
            + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
