import os
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "💰 <b>Конвертер валют</b>\n\n"
        "Отправьте сумму и валюты в формате:\n"
        "<code>100 USD to RUB</code>\n\n",
        parse_mode="HTML"
    )

@dp.message()
async def convert_currency(message: types.Message):
    try:
        text = message.text.upper()
        amount, from_currency, _, to_currency = text.split()
        amount = float(amount)
    except:
        await message.answer("Неверный формат. Пример:\n<code>100 USD to RUB</code>", parse_mode="HTML")
        return

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data.get("result") == "success":
                result = data["conversion_result"]
                rate = data["conversion_rate"]
                await message.answer(
                    f"🔹 <b>Результат:</b>\n"
                    f"{amount} {from_currency} = {round(result, 2)} {to_currency}\n"
                    f"Курс: 1 {from_currency} = {round(rate, 4)} {to_currency}",
                    parse_mode="HTML"
                )
            else:
                await message.answer("Ошибка API. Попробуйте позже.")

@dp.callback_query()
async def button_handler(callback: types.CallbackQuery):
    from_currency, to_currency = callback.data.split("_")
    await callback.message.answer(f"Введите сумму для конвертации {from_currency} → {to_currency}:")

async def main():
    await dp.start_polling(bot)
asyncio.run(main())