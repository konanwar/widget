

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(input_string: str) -> str:
   """определяем что на входе(счет,карта)"""
   identifier = ''
   _digits = ''
   for i in input_string:
      if i.isalpha():
         identifier += i
      elif i.isdigit():
         _digits += i
   if identifier == 'Счет':
      print(identifier, get_mask_account(_digits))
   else:
      print(identifier, get_mask_card_number(_digits))


input_string = str(input())
mask_account_card(input_string)