from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

API_TOKEN = '' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class DealForm(StatesGroup):
    company_name = State()
    deal_info = State()

@dp.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await message.answer("Добрый день!")
    await message.answer("Введите название компании")
    await state.set_state(DealForm.company_name)

@dp.message(DealForm.company_name)
async def handle_company_name(message: Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await message.answer("")
    await state.set_state(DealForm.deal_info)

@dp.message(DealForm.deal_info)
async def handle_deal_info(message: Message, state: FSMContext):
    data = await state.get_data()
    company_name = data.get()
    deal_info = message.text

    await message.answer(f"Название компании: {company_name}")
    await asyncio.sleep(2)
    await message.answer(f"Информация о сделке: {deal_info}")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
