from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

router = Router()

def menu_button_builder():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='▶Главное меню', callback_data = 'menu')]
    ])
    return kb

def menu_builder():
    text = '<b>ГЛАВНОЕ МЕНЮ</b> \n' \
    'Тут ты можешь поменять: \n' \
    '<b>1.</b> Айди тгк из которого нужно пастить \n' \
    '<b>2.</b> Айди тгк в который будет приходить паста \n\n' \
    '<span class="tg-spoiler">Автор: @vuaaeoeoeoeoeopoppypypypruejdbcb </span>'
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = '1️⃣ Сменить айди тгк с пастой', callback_data = 'change_pasta_id')], [InlineKeyboardButton(text = '2️⃣ Сменить айди тгк для пасты', callback_data = 'change_to_pasta_id')]
    ])
    return text, kb

@router.message(CommandStart())
async def start_handler(message: Message):
    kb = menu_button_builder()
    await message.reply('<b>Привет</b> \n' \
    '<i>Это бот для копипастинга сообок.</i> \n' \
    '<i>переходи в главное меню, и настраивай бота.</i>',
    parse_mode = 'HTML',
    reply_markup=kb)

@router.callback_query(F.data == 'menu')
async def menu_button_handler(callback: CallbackQuery):
    text, kb = menu_builder()
    await callback.message.edit_text(text, parse_mode='HTML', reply_markup = kb)

@router.message(Command('menu'))
async def menu_command_handler(message: types.Message):
    text, kb = menu_builder()
    await message.answer(text, parse_mode='HTML', reply_markup = kb)
