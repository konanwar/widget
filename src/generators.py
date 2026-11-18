from typing import Iterable, Dict, Any


def filter_by_currency(records: Iterable[dict[str, Any]], currency: str = "USD") -> Iterable[dict[str, Any]]:
    """поочередно выдает транзакции c USD """
    if not isinstance(records, list):
        raise TypeError("Ожидается список словарей")

    for record in records:
        operation_amount = record.get("operationAmount",{})
        valid_corr = operation_amount.get("currency",{})
        code = valid_corr.get('code') or ''
        if code.upper() == currency.upper():
           yield record
# def transaction_descriptions(records: list[dict], description: str ):
#    """возвращает описание каждой операции по очереди"""
#
#
#
# def card_number_generator(start, end):
#     """номера банковских карт в формате XXXX XXXX XXXX XXXX"""
#     pass