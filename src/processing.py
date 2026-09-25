from typing import List, Dict, Any


def filter_by_state(records: List[Dict[str, Any]], state="EXECUTED") -> List[Dict[str, Any]]:
    """функуия возвращает новый список словарей по ключу 'state'"""
    filter_records = []
    for operation in records:
        if operation["state"] == state:
            filter_records.append(operation)
    return filter_records


def sort_by_date(records: List[Dict[str, Any]], _sort: bool=True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(records, key=lambda d: d.get("date"), reverse=_sort)


_sort = None
state = None
records = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
if state is None:
    print(
        filter_by_state(
            records,
        )
    )
else:
    print(filter_by_state(records, state))


if _sort is None:
    print(
        sort_by_date(
            records,
        )
    )
else:
    print(sort_by_date(records, _sort))
