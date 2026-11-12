from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счёта в строке вида «Visa Platinum 7000792289606361».

    Возвращает строку с замаскированным номером: «Visa Platinum 7000 79** **** 6361».
    """
    if not isinstance(info, str):
        raise TypeError("Входные данные должны быть строкой")

    info = info.strip()
    if not info:
        raise ValueError("Входная строка пуста")

    # Разделяем строку на название (тип) и номер: номер — последняя «часть» из цифр
    parts = info.rsplit(" ", 1)

    if len(parts) != 2 or not parts[1].isdigit():
        raise ValueError(f"Некорректный формат строки: {info!r}")

    name, number = parts[0], parts[1]

    # 20 цифр — счёт, 16 цифр — карта
    if len(number) == 20:
        masked_number = get_mask_account(number)
    elif len(number) == 16:
        masked_number = get_mask_card_number(number)
    else:
        raise ValueError(
            f"Номер должен содержать 16 цифр (карта) или 20 (счёт), получено {len(number)}"
        )

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO 8601 («2024-03-11T02:26:18.671407») в «ДД.ММ.ГГГГ»."""
    from datetime import datetime

    if not isinstance(date_str, str):
        raise TypeError("Дата должна быть строкой")

    if not date_str:
        raise ValueError("Входная строка даты пуста")

    try:
        parsed = datetime.fromisoformat(date_str)
    except ValueError as e:
        raise ValueError(f"Некорректный формат даты: {date_str!r}") from e

    return parsed.strftime("%d.%m.%Y")