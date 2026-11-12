from datetime import datetime


def filter_by_state(records: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа state."""
    if not isinstance(records, list):
        raise TypeError("Ожидается список словарей")
    return [item for item in records if item.get("state") == state]


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по ключу date (формат ISO 8601).

    По умолчанию — по убыванию (reverse=True), reverse=False — по возрастанию.
    :rtype: list[dict]
    """
    if not isinstance(records, list):
        raise TypeError("Ожидается список словарей")

    # Валидация всех элементов до сортировки
    for item in records:
        if not isinstance(item, dict):
            raise TypeError(f"Элемент списка должен быть словарём, получено {type(item).__name__}")
        if "date" not in item:
            raise KeyError("В словаре отсутствует ключ 'date'")
        try:
            datetime.fromisoformat(item["date"])
        except (ValueError, TypeError) as e:
            raise ValueError(f"Некорректная дата: {item['date']!r}") from e

    return sorted(records, key=lambda d: d["date"], reverse=reverse)
