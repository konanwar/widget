from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """определяем что на входе(счет,карта)"""
    identifier = ""
    _digits = ""
    for i in input_string:
        if not i.isdigit():
            identifier += i
        elif i.isdigit():
            _digits += i
    if identifier == "Счет":
        return identifier + get_mask_account(_digits)
    else:
        return identifier + get_mask_card_number(_digits)


def get_date(input_data: str) -> str:
    """передает в требуемом формате дату по заданию"""
    dt = datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


def get_date_now(input_data: str) -> str:
    """передает  дату ввода реквизитов"""
    dt = datetime.strptime(input_data, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


input_string = str(input("ведите реквизиты"))
input_data = str(input("введите дату"))
print(mask_account_card(input_string))
input_data_now = str(datetime.now())
print(get_date(input_data))
print(get_date_now(input_data_now))
# print(input_data)
