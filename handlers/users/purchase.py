from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline.buttons import *
from loader import dp
from aiogram import types
import emoji
from media import *
import asyncio


@dp.message_handler(Command('items'))
async def show_menu(message: Message):
    await message.answer(text="welcome", reply_markup=open_catalog)


@dp.callback_query_handler(text=['menu'])
async def choose_category(call: CallbackQuery):
    await call.message.answer(text='choose item category', reply_markup=category)


@dp.inline_handler(text='meat')
async def empty_query(query: types.InlineQuery):
    print('111111111111111111111111111111111111111111')
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                thumb_url='http://i.piccy.info/i9/6464abc45b1071c471b104c29962b129/1630105461/113969/1440070/citrus_jerky.jpg',
                description='100г. - 75 грн, 200г. - 145 грн,\n500г. - 340 грн, 1кг. - 650 грн',
                title=emoji.emojize('Куриные джерки цитрус :lemon::tangerine:'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="2",
                thumb_url='https://i.piccy.info/i9/d86403de705930a477d56adadeea4f86/1630138139/140143/1440065/dijon_jerky_800.jpg',
                description='100г. - 75 грн, 200г. - 145 грн,\n500г. - 340 грн, 1кг. - 650 грн',
                title=emoji.emojize('Куриные джерки дижонская горчица'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="3",
                thumb_url='http://i.piccy.info/i9/7e76e8405394cb2ccc4f08195ec935f3/1630101139/116773/1440065/bbq_jerky.jpg',
                description='100г. - 75 грн, 200г. - 145 грн,\n500г. - 340 грн, 1кг. - 650 грн',
                title=emoji.emojize('Куриные джерки BBQ'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="4",
                thumb_url='http://i.piccy.info/i9/7b18f276c4b4e53010e58d344099f69b/1630105376/138216/1440070/jerky_teriyaki.jpg',
                description='100г. - 100 грн, 200г. - 190 грн,\n500г. - 460 грн, 1кг. - 900 грн',
                title=emoji.emojize('Говяжьи джерки терияки'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="5",
                thumb_url='https://i.piccy.info/i9/71dfb52b5869a708f8ef57dc755d0bbe/1630138430/130395/1440065/66975jerky_adjika_800.jpg',
                description='100г. - 75 грн, 200г. - 145 грн,\n500г. - 340 грн, 1кг. - 650 грн',
                title=emoji.emojize('Куриные джерки аджика'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="6",
                thumb_url='https://i.piccy.info/i9/deacb75af41b7892c50ade705987ad6d/1630138641/125617/1440065/jerky_gov_800.jpg',
                description='100г. - 100 грн, 200г. - 190 грн,\n500г. - 460 грн, 1кг. - 900 грн',
                title=emoji.emojize('Говяжьи джерки'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="7",
                thumb_url='https://i.piccy.info/i9/2d53db7f88d67585b21bd7af751e1f33/1630138919/123060/1440065/pork_jerky_800.jpg',
                description='100г. - 85 грн, 200г. - 165 грн,\n500г. - 390 грн, 1кг. - 750 грн',
                title=emoji.emojize('Свиные джерки кореандр'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="8",
                thumb_url='https://i.piccy.info/i9/c4d42be55c8aed24f6720dbf2c179bc9/1630139106/118388/1440065/pork_bbq_800.jpg',
                description='100г. - 85 грн, 200г. - 165 грн,\n500г. - 390 грн, 1кг. - 750 грн',
                title=emoji.emojize('Свиные джерки BBQ'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
        ],
        cache_time=5
    )


@dp.inline_handler(text='sausages')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="9",
                thumb_url='https://i.piccy.info/i9/4be34a5ef80b54a543dd6bb2333410e9/1630141231/107259/1440065/sausages_teriyaki_800.jpg',
                description='100г. - 75 грн, 200г. - 145 грн,\n500г. - 340 грн, 1кг. - 650 грн',
                title=emoji.emojize('Колбаски терияки'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="10",
                thumb_url='https://i.piccy.info/i9/78692e8801b8375a41c750c73da61794/1630141423/127249/1440065/pork_sausages_800.jpg',
                description='100г. - 85 грн, 200г. - 165 грн,\n500г. - 390 грн, 1кг. - 750 грн',
                title=emoji.emojize('Свиные колбаски кореандр'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="11",
                thumb_url='https://i.piccy.info/i9/55634ddb6cf7e2b69d64bbbaa15c359c/1630141645/124929/1440065/sausages_chorizo_800.jpg',
                description='100г. - 85 грн, 200г. - 165 грн,\n500г. - 390 грн, 1кг. - 750 грн',
                title=emoji.emojize('Свиные колбаски чоризо'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
        ],
        cache_time=5
    )


@dp.inline_handler(text='sets')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="12",
                thumb_url='https://i.piccy.info/i9/35f2fec2ac178637af7f3073c0d4de4d/1630142009/132626/1440079/set_800.jpg',
                description='400г.(по 30г. кадого вида) - 350 грн',
                title=emoji.emojize('House of jerky set - S'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="13",
                thumb_url='https://i.piccy.info/i9/35f2fec2ac178637af7f3073c0d4de4d/1630142009/132626/1440079/set_800.jpg',
                description='600г.(по 45г. кадого вида) - 500 грн',
                title=emoji.emojize('House of jerky set - M'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
            types.InlineQueryResultArticle(
                id="14",
                thumb_url='https://i.piccy.info/i9/35f2fec2ac178637af7f3073c0d4de4d/1630142009/132626/1440079/set_800.jpg',
                description='850г.(по 65г. кадого вида) - 700 грн',
                title=emoji.emojize('House of jerky set - L'),
                input_message_content=types.InputMessageContent(
                    message_text="Chicken jerky"
                ),
            ),
        ],
        cache_time=5
    )

