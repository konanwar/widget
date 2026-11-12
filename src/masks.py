def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты: 7000 79** **** 6361.

    Пробелы и дефисы во входной строке игнорируются.
    Номер должен состоять ровно из 16 цифр, иначе — ошибка.
    """
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")

    # Оставляем только цифры (на случай пробелов/дефисов во входных данных)
    digits = "".join(ch for ch in card_number if ch.isdigit())

    if len(digits) != 16:
        raise ValueError(
            f"Номер карты должен содержать 16 цифр, получено {len(digits)}"
        )

    # Первые 4 цифры, вторые 2 цифры, затем звёздочки, последние 4 цифры
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счёта: **4305.

    Номер должен состоять ровно из 20 цифр, иначе — ошибка.
    """
    if not isinstance(account, str):
        raise TypeError("Номер счёта должен быть строкой")

    # Оставляем только цифры (на случай пробелов, дефисов и т.п.)
    digits = "".join(ch for ch in account if ch.isdigit())

    if len(digits) != 20:
        raise ValueError(
            f"Номер счёта должен содержать 20 цифр, получено {len(digits)}"
        )

    return f"**{digits[-4:]}"
