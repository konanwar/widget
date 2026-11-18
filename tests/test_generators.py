import pytest
from mypy.nativeparse import expect_tag

from src.generators import filter_by_currency #,transaction_descriptions,card_number_generator


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



# def test_transaction_descriptions(self, transaction_descriptions: list[dict]): -> None
#     b = transaction_descriptions()
#     pass



# def test_card_number_generator(self, card_number_generator: list[dict]): -> None
#     c = card_number_generator()
#     pass