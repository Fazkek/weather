import requests
import time
import asyncio
import datetime
import threading
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import date
from bs4 import BeautifulSoup
import re

token = "5787139770:AAG6WQN12KsIKLYCah2iDXTJjobSeiw7aiI"


def timew():
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    s_time = current_time.split(":")
    a = int(s_time[0])
    b = int(s_time[1])
    aft = 24*60-(60*a + b)
    return aft


def sec():
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    s_time = current_time.split(":")
    c = s_time[2].split('.')
    c = int(c[0])

    return c


def weather():
    pog = "https://ru-meteo.ru/izhevsk/hour"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for temp in soup.find_all('div', class_="current-temp"):
        temp = temp.text
        temp = temp.split('.')
        temp = temp[0]
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    current_time = current_time.split('.')
    current_time = current_time[0]
    current_time = current_time.split(':')
    current_time.pop(2)
    current_time = current_time[0] + ":" + current_time[1]

    current_date = str(date.today())
    current_date = current_date.split('-')
    current_date = current_date[2] + '.' + current_date[1]
    timew = f'{current_date}   {current_time}'
    for obl in soup.find('td', class_='dsr t-10'):
        obl = obl.text.split(',')
        obl = obl[0]
        if obl == "Ясно":
            obl = obl + "☀️"
        if obl == "Пасмурно":
            obl = obl + "☁️️"
        if obl == "Преимущественно облачно":
            obl = obl + "🌥️"
        if obl == "Слабый снег":
            obl = obl + "🌨️"
        if obl == "Незначительная облачность":
            obl = obl + "🌤"
    for real_temp in soup.find_all('div', class_='current-temp'):
        for real_temp in soup.find_all('span', class_='apparent'):
            real_temp = real_temp.text.split()
            real_temp = real_temp[2].split('°')
            real_temp = real_temp[0]
    for wind_max in soup.find_all('div', class_="main"):
        for wind_max in soup.find_all('li', title="Ветер в румбах горизонта  (откуда дует)"):
            wind_max = wind_max.text.split()
            wind_max = wind_max[6]
    for wind in soup.find_all('div', class_="main"):
        for wind in soup.find_all('li', title="Ветер в румбах горизонта  (откуда дует)"):
            wind = wind.text.split()
            wind = wind[1]
    for wla in soup.find('td', class_="hmid t-8"):
        wla = wla.text
    weather_info = '✋Погода в Ижевске: ' + '\n' + '🌡' + temp +'C' + f' ({real_temp}°C), ' + obl + '\n' + '💦Влажность - ' + wla + '\n' + f'🌬Ветер - {wind} м/с' + f' (max - {wind_max} м/с)' + '\n' + f'Данные на {timew}'
    return weather_info


def clothes():
    pog = "https://ru-meteo.ru/izhevsk/hour"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for temp in soup.find_all('div', class_="current-temp"):
        temp = temp.text
        temp = temp.split('.')
        temp = temp[0]
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    current_time = current_time.split('.')
    current_time = current_time[0]
    current_time = current_time.split(':')
    current_time.pop(2)
    current_time = current_time[0] + ":" + current_time[1]

    current_date = str(date.today())
    current_date = current_date.split('-')
    current_date = current_date[2] + '.' + current_date[1]
    timew = f'{current_date}   {current_time}'
    for obl in soup.find('td', class_='dsr t-10'):
        obl = obl.text.split(',')
        obl = obl[0]
        if obl == "Ясно":
            obl = obl + "☀️"
        if obl == "Пасмурно":
            obl = obl + "☁️️"
        if obl == "Преимущественно облачно":
            obl = obl + "🌥️"
        if obl == "Слабый снег":
            obl = obl + "🌨️"
        if obl == "Незначительная облачность":
            obl = obl + "🌤"
    for real_temp in soup.find_all('div', class_='current-temp'):
        for real_temp in soup.find_all('span', class_='apparent'):
            real_temp = real_temp.text.split()
            real_temp = real_temp[2].split('°')
            real_temp = real_temp[0]
    for wind_max in soup.find_all('div', class_="main"):
        for wind_max in soup.find_all('li', title="Ветер в румбах горизонта  (откуда дует)"):
            wind_max = wind_max.text.split()
            wind_max = wind_max[6]
    for wind in soup.find_all('div', class_="main"):
        for wind in soup.find_all('li', title="Ветер в румбах горизонта  (откуда дует)"):
            wind = wind.text.split()
            wind_fix = int(wind[1])

    real_temp = real_temp.split('−')
    real_temp = int(real_temp[1])
    real_temp = real_temp * -1

    if -5 <= real_temp <= -1:
        if wind_fix >= 5:

            a = "Сегодня не очень холодно и ветренно"
            b = "Я советую надеть вам шапку, капюшон и шарф"

            return a, b
        else:

            a = "Сегодня не очень холодно"
            b = "Я советую надеть вам шапку"

            return a, b
    if -10 <= real_temp <= -6:
        if wind_fix >= 5:

            a = "Сегодня прохладно и ветренно"
            b = "Я советую надеть вам тёплую шапку, шарф, капюшон и перчатки"

            return a, b
        else:

            a = "Сегодня прохладно"
            b = "Я советую надеть вам тёплую шапку и перчатки"

            return a, b
    if -15 <= real_temp <= -11:
        if wind_fix >= 5:

            a = "Сегодня холодно и ветренно"
            b = "Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, капюшон и куртку до колена"

            return a, b
        else:

            a = "Сегодня холодно"
            b = "Я советую вам надеть подштанники, тёплую шапку, перчатки и куртку до колена"
            return a, b

    if -20 <= real_temp <= -16:
        if wind_fix >= 5:
            print("Сегодня правда холодно и ветренно")
            print("Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, кофту, капюшон и куртку до колена")

            a = "Сегодня правда холодно и ветренно"
            b = "Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, кофту, капюшон и куртку до колена"

            return a, b
        else:

            a = "Сегодня правда холодно"
            b = "Я советую вам надеть подштанники, тёплую шапку, перчатки, кофту и куртку до колена"

            return a, b
    if -25 <= real_temp <= -21:
        if wind_fix >= 5:

            a = "Сегодня очень холодно и ветренно"
            b = "Я советую вам не выходить из дома"

            return a, b
        else:

            a = "Сегодня очень холодно"
            b = "Я советую вам надеть надеть подштанники, тёплую шапку, перчатки, кофту и куртку до колена"

            return a, b


clothes()


def money():
    pog = "https://www.banki.ru/products/currency/cash/usd/izhevsk/"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for usd in soup.find_all('td', class_="currency-table__rate currency-table__darken-bg"):
        usd = usd.find('div', class_="currency-table__large-text")
        usd = usd.text
        usd = f"{usd} ₽"
        return usd


def money_euro():
    pog = "https://www.banki.ru/products/currency/eur/"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for euro in soup.find_all('td', class_="currency-table__rate currency-table__darken-bg"):
        euro = euro.find('div', class_="currency-table__large-text")
        euro = euro.text
        euro = f"{euro} ₽"
        return euro


def btc():
    pog = "https://mainfin.ru/crypto/bitcoin"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for btc in soup.find_all('div', class_="crypto_curr_val"):
        btc = btc.text

        return btc


def info():
    euro_ = money_euro()
    weather_ = weather()
    clothes_ = clothes()
    btc_ = btc()
    usd_ = money()
    text = f"{weather_} \n ******************************** \n ❄️{clothes_[0]}❄️ \n ❗️{clothes_[1]}❗️\n ******************************** \n 💰Биткоин: {btc_} \n 💵Доллар: {usd_} \n 💶Евро: {euro_}"
    return text


bot = Bot(token=token)
dp = Dispatcher(bot)


def main_bot(dp):
    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message, markup=None):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Информация")
        keyboard.add(button_1)
        await message.answer(f"✋Привет! Моя главная задача, заключается в облегчении твоих утренних дел. Я буду отправлять тебе сводку погоды, одежды, которую тебе надо надеть, и курсы валют. Чтобы получить сообщение утром и настроить время, следуй моим инструкциям: \n\n ❗️Чтобы сообщение отправлялось в нужное время - просто отправьте мне его, в подобном формате 7:00\n\n ❗️Если найдёшь какие то недочёты или бот не работает пиши сюда -> @fazk4ek", reply_markup=keyboard)

    @dp.message_handler(content_types=['text'])
    async def main(message: types.Message):

        if message.text == 'Информация':
            a = info()
            a_s = a.split('********************************')
            await bot.send_message(message.chat.id,
                             text=a_s[0])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                             text=a_s[1])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                             text=a_s[2])
            time.sleep(0.8)
            await bot.send_message(message.chat.id,
                             text="Желаю вам продуктивного дня)")

        elif message.text == "Настройка времени":
            time.sleep(0.3)
            await bot.send_message(message.chat.id,
                             text="Отправьте время в таком формате - 7:00")
            time.sleep(0.3)
            await bot.send_message(message.chat.id,
                             text="Если хотите поменять время - просто отправьте мне его")

        elif (re.match(r'([12]\d[:][0-5]\d)|([1-9][:][0-5]\d)', message.text)) is None:
            await bot.send_message(message.chat.id,
                                   text="Нет такой команды!")
        else:
            a = timew()
            c = sec()
            time.sleep(0.3)

            n_time = message.text
            n_time = n_time.split(':')
            z = int(n_time[0])
            v = int(n_time[1])
            x = a + (z*60+v)
            if x > 1440:
                x = x - 1440
            await bot.send_message(message.chat.id, text="Таймер установлен!")
            await asyncio.sleep(x*60-c-2)
            a = info()
            a_s = a.split('********************************')
            await bot.send_message(message.chat.id,
                                   text="Время истекло!")
            time.sleep(1)
            await bot.send_message(message.chat.id,
                                   text=a_s[0])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text=a_s[1])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text=a_s[2])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text="Желаю вам продуктивного дня)")


if __name__ == '__main__':
    th2 = threading.Thread(target=main_bot, args=(dp,), daemon=True)
    th2.start()
    executor.start_polling(dp, skip_updates=True)