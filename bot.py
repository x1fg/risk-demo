from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class DealForm(StatesGroup):
    company_name = State()
    deal_info = State()

@dp.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await message.answer("Добрый день!\nВас приветсвует агентная система оценки рисков.")
    await asyncio.sleep(1)
    await message.answer('Введите название компании.\nПример: "ОАО Демо компания".')
    await state.set_state(DealForm.company_name)

@dp.message(DealForm.company_name)
async def handle_company_name(message: Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await message.answer(
        "*Получение данных по сделке*\n\n"
        "🔍 Обращение к:\n\n"
        "• АС Байкал\n"
        "• Risk RAG\n"
        "• FS Online\n",
        parse_mode="Markdown"
    )
    await asyncio.sleep(2)
    await message.answer('Данные по сделке успешно получены из систем.')
    await asyncio.sleep(1)
    await message.answer('Введите дополнительные подробности сделки(оционально).\n\nЕсли дополнительных подробностей нет, введите:\n "Нет дополнительной информации."')
    await state.set_state(DealForm.deal_info)

@dp.message(DealForm.deal_info)
async def handle_deal_info(message: Message, state: FSMContext):
    data = await state.get_data()
    company_name = data.get('company_name')
    #deal_info = message.text
    await message.answer(f"*Начало процесса оценки рисков.*", parse_mode="Markdown")
    await asyncio.sleep(1)
    await message.answer(f"Запуск Кредитной машины ЮЛ, AEF.")
    await asyncio.sleep(1)
    await message.answer(f"Векторизация полученной информации.")
    await asyncio.sleep(1)
    await message.answer(f"⚙️Вызов Агента Эксперт оценки маркетингового риска.")
    await asyncio.sleep(1)
    await message.answer(
        "*Обращение к внешним данным для получения дополнительной информации:*\n\n"
        "• БКИ\n"
        "• Операторы сотовой связи\n"
        "• Госорганы\n"
        "• Внешний скоринг\n"
        "• Соцсети",
        parse_mode="Markdown"
    )
    await asyncio.sleep(1)
    await message.answer(f"⚙️Вызов Агента Эксперт деловой репутации")
    await asyncio.sleep(1)
    await message.answer(
        "*Выбор необходимых инструментов:*\n\n"
        "• API анализ ФЛ\n"
        "• API доступ к правовой информации\n"
        "• API поиск\n",
        parse_mode="Markdown"
    )
    await asyncio.sleep(1)
    await message.answer("Необходимо проанализировать Акционеров, Бенифициаров и Лиц принимающих решение.")
    await asyncio.sleep(1)
    await message.answer(f"Обращение к Кредитной машине ФЛ, AEF")
    await message.answer(f"⚙️Вызов Агента Оценки ФЛ")
    await asyncio.sleep(1)
    await message.answer(
        "Получение заключения от Агента ФЛ"
    )
    await message.answer(f"Формирование финального заключения")
    await asyncio.sleep(3)
    await message.answer(
    "📄*Заключение по оценке кредитоспособности компании:*\n\n"
        "*Общие параметры сделки:*\n"
        "• **Сумма кредита**: 100 миллионов рублей\n"
        "• **Срок кредитования**: 10 лет\n\n"
        "*Оценка рисков:*\n"
        "• *Маркетинговый риск*: Средний\n"
        "Риск связан с колебаниями спроса в отрасли. Хотя компания занимает стабильное положение, высокая конкуренция и экономическая волатильность могут повлиять на результаты.\n\n"
        "• *Риск деловой репутации*: Высокий\n"
        "У компании имеются случаи судебных разбирательств и конфликты с контрагентами, что может негативно сказаться на её обязательствах перед кредиторами.\n\n"
        "*Заключение:*\n"
        "На основании представленной информации, *рекомендуется отказать в предоставлении кредита* ввиду высокого уровня риска деловой репутации и средних маркетинговых рисков.",
        parse_mode="Markdown"
    )
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
