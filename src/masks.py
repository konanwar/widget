def get_mask_card_number(card_number: str) -> str:
    """маскировка номера банковской карты"""

    # Оставляем только цифры (на случай пробелов/дефисов во входных данных)
    digits = "".join(ch for ch in card_number if ch.isdigit())

    if len(digits) < 10:
        # Слишком короткий номер — нельзя показать 6+4 цифры
        return "*" * len(digits)

    # Первые 6 цифр, последние 4 цифры
    first_part = digits[:6]
    last_part = digits[-4:]

    # Средняя часть: всё, что между ними, заменяем на *
    middle_part = "*" * (len(digits) - 10)

    full_masked = first_part + middle_part + last_part

    # Разбиваем на блоки по 4 символа через пробел
    blocks = [full_masked[i : i + 4] for i in range(0, len(full_masked), 4)]
    return " ".join(blocks)


def get_mask_account(account: str) -> str:
    """маскировка номера банковского счета"""

    # Оставляем только цифры (на случай пробелов, дефисов и т.п.)
    digits = "".join(ch for ch in account if ch.isdigit())

    if len(digits) <= 4:
        # Если цифр 4 или меньше — показываем их все, а звёздочек столько, сколько не хватает до 4
        return "*" * (4 - len(digits)) + digits

    # Берём последние 4 цифры
    last_four = digits[-4:]
    return f"**{last_four}"


# card_number= input()
# account = input()
#print(get_mask_card_number("1234567890123456"))
#print(get_mask_account("123456789012"))
