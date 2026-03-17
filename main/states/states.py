from aiogram.fsm.state import StatesGroup, State

class Change(StatesGroup):
    wait_pasta_id = State()
    wait_for_pasta_id = State()