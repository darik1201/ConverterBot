# Converter Bot

## Описание
Это Telegram-бот для конвертации валют, использующий API ExchangeRate-API. Бот позволяет конвертировать суммы между различными валютами по текущему курсу.
![image](https://github.com/user-attachments/assets/156c8922-4433-4445-933a-732442653b3b)

## Функционал
- Конвертация валют по команде
- Поддержка всех основных мировых валют
- Отображение текущего курса обмена
- Простое и интуитивно понятное взаимодействие

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий/currency-converter-bot.git
   cd currency-converter-bot
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте ваши токены:
   ```
   BOT_TOKEN=ваш_telegram_bot_token
   API_KEY=ваш_exchangerate_api_key
   ```

4. Запустите бота:
   ```bash
   python bot.py
   ```

## Использование
Отправьте боту сообщение в формате:
```
<сумма> <валюта_из> to <валюта_в>
```
Например:
```
100 USD to RUB
```

## Технологии
- Python 3.9+
- aiogram 3.x (асинхронный фреймворк для Telegram Bot API)
- ExchangeRate-API (для получения курсов валют)
- aiohttp (для асинхронных HTTP-запросов)

## Лицензия
MIT License
