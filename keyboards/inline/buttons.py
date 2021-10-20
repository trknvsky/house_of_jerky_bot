from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

open_catalog = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text='open catalog', callback_data='menu')
       ] 
    ]
)

category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='meat', callback_data='meat'),
            InlineKeyboardButton(text='sets', callback_data='sets'),
            InlineKeyboardButton(text='sausages', callback_data='sausages')
        ]
    ]
)
