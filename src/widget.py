

from src.masks import get_mask_card_number
from src.masks import get_mask_account
from datetime import datetime


def mask_account_card(input_string: str) -> str:
   """определяем что на входе(счет,карта)"""
   identifier = ''
   _digits = ''
   for i in input_string:
      if  not i.isdigit():
         identifier += i
      elif i.isdigit():
         _digits += i
   if identifier == 'Счет':
      print(identifier, get_mask_account(_digits))
   else:
      print(identifier, get_mask_card_number(_digits))

def get_date(input_data: str)-> str:
    dt = datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S.%f")
    print(dt.strftime("%d.%m.%Y"))  # 11.03.2024

input_string = str(input('ведите реквизиты'))
input_data = str(input('введите дату'))
mask_account_card(input_string)
get_date(input_data)