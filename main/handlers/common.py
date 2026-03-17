from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import Change
from handlers import settings
import config

router = Router()

def cansel_builder():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = 'Отмена', callback_data = 'cansel')]
    ])
    return kb

@router.callback_query(F.data == 'cansel')
async def cansel_handler(callback: CallbackQuery, state: FSMContext):
    kb = settings.menu_button_builder()
    await state.clear()
    await callback.message.answer('Отменено', reply_markup = kb)
    await callback.answer()

@router.callback_query(F.data == 'change_pasta_id')
async def change_pasta_id(callback: CallbackQuery, state: FSMContext):
    kb = cansel_builder()
    await callback.message.answer('<i>Скинь сюда айди тгк, с которого будут паститься сообщения \n' \
    'Узнать его можешь прислав ответом сообщение из этого тгк, в</i> - @FIND_MY_ID_BOT', 
    parse_mode='HTML',
    reply_markup=kb)
    await state.set_state(Change.wait_pasta_id)
    await callback.answer()

@router.message(Change.wait_pasta_id)
async def save_pasta_id(message: types.Message, state: FSMContext):
    kb = settings.menu_button_builder()
    new_data = message.text.strip()
    config.update_config('TARGET_CHAT', new_data)
    await message.answer(f'<i>Вы сменили старый айди чата с пастой, на</i> - {new_data}',parse_mode='HTML', reply_markup = kb)
    await state.clear()

@router.callback_query(F.data == 'change_to_pasta_id')
async def change_to_pasta_id(callback: CallbackQuery, state: FSMContext):
    kb = cansel_builder()
    await callback.message.answer('<i>Скинь сюда айди тгк, в который добавлен этот бот со всеми правами, и в который будут приходить паста \n' \
    'Узнать его можешь прислав ответом сообщение из этого тгк, в </i> - @FIND_MY_ID_BOT',
    parse_mode='HTML',
    reply_markup=kb)
    await state.set_state(Change.wait_for_pasta_id)
    await callback.answer()

@router.message(Change.wait_for_pasta_id)
async def save_for_pasta_id(message: types.Message, state: FSMContext):
    kb = settings.menu_button_builder()
    new_data = message.text.strip()
    config.update_config('SOURSE_CHAT', new_data)
    await message.answer(f'<i>Вы сменили старый айди чата для пасты, на</i> - {new_data}',parse_mode='HTML', reply_markup = kb)
    await state.clear()

