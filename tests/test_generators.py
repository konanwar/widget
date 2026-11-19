import pytest
from mypy.nativeparse import expect_tag

from src.generators import filter_by_currency ,transaction_descriptions ,card_number_generator


def test_filter_by_currency_USD(for_test_generators: list[dict] ) -> None:
    result = (filter_by_currency(for_test_generators, currency='USD'))
    """ логика сортировки"""
    assert {item["id"] for item in result} == {939719570, 142264268, 895315941}



def test_filter_by_currency_RUB(for_test_generators: list[dict] ) -> None:
    """ проверка на регистр"""
    result = (filter_by_currency(for_test_generators, currency='rub'))
    assert {item["id"] for item in result} == {873106923, 594226727}


def test_filter_by_corrency_by_generators(for_test_generators):
    """проверка генератора на поочередный вывод и соответсвие строк"""
    result = (filter_by_currency(for_test_generators, currency='rub'))
    assert next(result) == {
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
        }
    assert next(result) == {
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

    # assert next(result['id']) == '873106923'
    # assert next(result['id']) == '594226727'

def test_filter_byby_currency_invalid_input() -> None:
    """Не-список на входе — TypeError."""
    with pytest.raises(TypeError):
        list(filter_by_currency(list[dict], "не список"))


def test_filter_by_currency_no_matching_currency(for_test_generators) -> None:
    """нет  в нужной валюте — пустой результат ."""
    result = filter_by_currency(for_test_generators, currency="KAZ")

    with pytest.raises(StopIteration):
        next(result)

    assert list(result) == []


transaction_NO_currency = {
        "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб."    # нет кода валюты

                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
    }
@pytest.mark.parametrize(
    'transaction, expected',
    [
        ([transaction_NO_currency],[]),
        ([],[])
     ],
)
def test_filter_by_currency_no_currency(transaction,expected ):
    """обработка на отсутвие кода валюты"""
    assert list(filter_by_currency(transaction,currency= 'USD')) == expected


class TestDescriptions:
    def test_transaction_descriptions(self, for_test_generators):
        """проверка работы функции"""
        descriptions = transaction_descriptions(for_test_generators)
        assert next(descriptions) == 'Перевод организации'
        assert next(descriptions) == 'Перевод со счета на счет'
        assert next(descriptions) == 'Перевод со счета на счет'
        assert next(descriptions) == 'Перевод с карты на карту'
        assert next(descriptions) == 'Перевод организации'

    transaction_NO_descriptions = {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб."  # нет кода валюты

            }
        },
                                                #"description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }

    @pytest.mark.parametrize(
        'transaction, expected',
        [
            ([transaction_NO_descriptions], []),
            ([], [])
        ],
    )
    def test_filter_by_currency_no_descriptions(self, transaction, expected):
        """обработка на пустой список, отсутвие описания перевода"""
        assert list(transaction_descriptions(transaction)) == expected



class TestCardNumberGenerator:
    def test_card_number_generator(self) -> None:
        """Генератор выдает номера по одному, в формате XXXX XXXX XXXX XXXX."""
        result = card_number_generator(1, 5)

        assert next(result) == "0000 0000 0000 0001"
        assert next(result) == "0000 0000 0000 0002"
        assert next(result) == "0000 0000 0000 0003"
        assert next(result) == "0000 0000 0000 0004"
        assert next(result) == "0000 0000 0000 0005"

        with pytest.raises(StopIteration):
            next(result)

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (1, 1, ["0000 0000 0000 0001"]),           # границы совпадают
            (9999999999999998, 9999999999999999,
             ["9999 9999 9999 9998", "9999 9999 9999 9999"]),  # верхняя граница
            (1111111111111111, 1111111111111112,
             ["1111 1111 1111 1111", "1111 1111 1111 1112"]),  # без ведущих нулей
        ],
    )
    def test_card_number_generator_ranges(self, start, stop, expected) -> None:
        assert list(card_number_generator(start, stop)) == expected

    @pytest.mark.parametrize(
        "start, stop",
        [
            (0, 5),          # ноль вне диапазона
            (1, 99999999999999999),  # больше максимума
            (5, 1),          # начало больше конца
        ],
    )
    def test_card_number_generator_invalid_range(self, start, stop) -> None:
        with pytest.raises(ValueError):
            list(card_number_generator(start, stop))

    def test_card_number_generator_type_error(self) -> None:
        with pytest.raises(TypeError):
            list(card_number_generator("1", "5"))