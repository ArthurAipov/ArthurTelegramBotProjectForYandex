from aiogram import Bot, Dispatcher, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='5811461408:AAHlqwi5pI1ggKqenxXe3o3M3cLupKpLCOk')
dp = Dispatcher(bot)

button_hello = KeyboardButton('Instruction')
button_youtube = KeyboardButton('Stations')
button_route = KeyboardButton('Route')

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_youtube, button_hello,
                                                          button_route)

button_first_station = KeyboardButton('Казань-Пасс')
button_second_station = KeyboardButton('Вахитово')
button_third_station = KeyboardButton('о.п. Березовая роща')
button_fourth_station = KeyboardButton('Комбинат')
button_fifth_station = KeyboardButton('о.п. Южный парк')
button_sixth_station = KeyboardButton('Юбилейная')
button_seventh_station = KeyboardButton('о.п. Столбище')
button_eighth_station = KeyboardButton('а/п Казань')
button_back = KeyboardButton('Назад')

keyboard_stations = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_stations.add(button_first_station, button_second_station)
keyboard_stations.add(button_third_station, button_fourth_station)
keyboard_stations.add(button_fifth_station, button_sixth_station)
keyboard_stations.add(button_seventh_station, button_eighth_station)
keyboard_stations.add(button_back)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply(
        'Здравствуйте! Вас приветствует Бот-Помощник. Я могу вам подсказать расписание электрички'
        + '\nДля просмотра команд введите - /help',
        reply_markup=keyboard1)


@dp.message_handler(commands=['information'])
async def information(message: types.Message):
    await message.reply(
        'все данные о маршрутах и расписаниях были взяты с сайта: https://kazan.tutu.ru/rasp.php?st1=116&st2=15916'
        + "\nСообщать о проблемах и несостыковках в расписании: @The_Arthur_one - контакт разработчика")


@dp.message_handler(commands=['help'])
async def information(message: types.Message):
    await message.reply(
        'Вот все основные команды:' + '\n /help - все доступные команды'
        + '\n /information - различная информация'
        + '\n /start - запуск бота')


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "Instruction":
        await message.reply(
            'Выбирете станцию у которой хотите посмотреть расписание, после посмотрите удобное для вас время.'
            ' Главное никуда не опоздайте)')
    elif message.text == 'Route':
        await message.answer_photo('https://vibirai.ru/image/1642839.jpg',
                                   "Как вы просили маршрут электропоезда: Казань-Пасс - а/п Казань")
    elif message.text == "Назад":
        await message.answer("Вы вернулись к началу", reply_markup=keyboard1)
    elif message.text == 'Казань-Пасс':
        await message.answer('Все времена отправления со станции Казань-Пасс - аэропорт Казань:'
                             + "\nКазань-Пасс—аэропорт Казань: 06:43"
                             + "\nКазань-Пасс—аэропорт Казань: 07:27"
                             + "\nКазань-Пасс—аэропорт Казань: 09:20"
                             + "\nКазань-Пасс—аэропорт Казань: 12:25"
                             + "\nКазань-Пасс—аэропорт Казань: 15:08"
                             + "\nКазань-Пасс—аэропорт Казань: 16:45"
                             + "\nКазань-Пасс—аэропорт Казань: 18:10"
                             + "\nКазань-Пасс—аэропорт Казань: 19:45")
    elif message.text == 'Вахитово':
        await message.answer('Все времена отправления со станции Вахитово:'
                             + "\n Из Вахитово в аэропорт Казань"
                             + "\nВахитово—аэропорт Казань: 06:47"
                             + "\nВахитово—аэропорт Казань: 07:31"
                             + "\nВахитово—аэропорт Казань: 09:24"
                             + "\nВахитово—аэропорт Казань: 12:29"
                             + "\nВахитово—аэропорт Казань: 15:12"
                             + "\nВахитово—аэропорт Казань: 16:49"
                             + "\nВахитово—аэропорт Казань: 18:14"
                             + "\nВахитово—аэропорт Казань: 19:49"
                             + "\n Из Вахитово в Казань-Пасс"
                             + "\nВахитово—Казань-Пасс: 06:35"
                             + "\nВахитово—Казань-Пасс: 07:53"
                             + "\nВахитово—Казань-Пасс: 09:02"
                             + "\nВахитово—Казань-Пасс: 11:54"
                             + "\nВахитово—Казань-Пасс: 14:09"
                             + "\nВахитово—Казань-Пасс: 16:50"
                             + "\nВахитово—Казань-Пасс: 17:49"
                             + "\nВахитово—Казань-Пасс: 19:18"
                             + "\nВахитово—Казань-Пасс: 20:54"
                             )
    elif message.text == 'о.п. Березовая роща':
        await message.answer('Все времена отправления со станции о.п. Березовая роща:'
                             + "\n Из о.п. Березовая роща в аэропорт Казань"
                             + "\nБерезовая роща—аэропорт Казань: 06:54"
                             + "\nБерезовая роща—аэропорт Казань: 07:38"
                             + "\nБерезовая роща—аэропорт Казань: 09:31"
                             + "\nБерезовая роща—аэропорт Казань: 12:36"
                             + "\nБерезовая роща—аэропорт Казань: 15:19"
                             + "\nБерезовая роща—аэропорт Казань: 16:56"
                             + "\nБерезовая роща—аэропорт Казань: 18:21"
                             + "\nБерезовая роща—аэропорт Казань: 19:56"
                             + "\n Из Березовая роща в Казань-Пасс"
                             + "\nБерезовая роща. — Казань-Пасс: 06:29"
                             + "\nБерезовая роща. — Казань-Пасс: 07:46"
                             + "\nБерезовая роща. — Казань-Пасс: 08:55"
                             + "\nБерезовая роща. — Казань-Пасс: 11:47"
                             + "\nБерезовая роща. — Казань-Пасс: 14:02"
                             + "\nБерезовая роща. — Казань-Пасс: 16:41"
                             + "\nБерезовая роща. — Казань-Пасс: 17:42"
                             + "\nБерезовая роща. — Казань-Пасс: 19:11"
                             + "\nБерезовая роща. — Казань-Пасс: 20:47"
                             )
    elif message.text == 'Комбинат':
        await message.answer('Все времена отправления со станции Комбинат:'
                             + "\n Из Комбинат в аэропорт Казань"
                             + "\nКомбинат—аэропорт Казань: 06:57"
                             + "\nКомбинат—аэропорт Казань: 07:41"
                             + "\nКомбинат—аэропорт Казань: 09:34"
                             + "\nКомбинат—аэропорт Казань: 12:39"
                             + "\nКомбинат—аэропорт Казань: 15:22"
                             + "\nКомбинат—аэропорт Казань: 16:59"
                             + "\nКомбинат—аэропорт Казань: 18:24"
                             + "\nКомбинат—аэропорт Казань: 19:59"
                             + "\n Из Комбинат в Казань-Пасс"
                             + "\nКомбинат—Казань-Пасс: 06:25"
                             + "\nКомбинат—Казань-Пасс: 07:43"
                             + "\nКомбинат—Казань-Пасс: 08:52"
                             + "\nКомбинат—Казань-Пасс: 11:44"
                             + "\nКомбинат—Казань-Пасс: 13:59"
                             + "\nКомбинат—Казань-Пасс: 16:38"
                             + "\nКомбинат—Казань-Пасс: 17:39"
                             + "\nКомбинат—Казань-Пасс: 19:08"
                             + "\nКомбинат—Казань-Пасс: 20:44"
                             )
    elif message.text == 'о.п. Южный парк':
        await message.answer('Все времена отправления со станции о.п. Южный парк:'
                             + "\n Из Южный парк в аэропорт Казань"
                             + "\nЮжный парк-аэропорт Казань: 07:00"
                             + "\nЮжный парк-аэропорт Казань: 07:44"
                             + "\nЮжный парк-аэропорт Казань: 09:37"
                             + "\nЮжный парк-аэропорт Казань: 12:42"
                             + "\nЮжный парк-аэропорт Казань: 15:25"
                             + "\nЮжный парк-аэропорт Казань: 17:02"
                             + "\nЮжный парк-аэропорт Казань: 18:27"
                             + "\nЮжный парк-аэропорт Казань: 20:02"
                             + "\n Из Южный парк в Казань-Пасс"
                             + "\nЮжный парк-Казань-Пасс: 06:22"
                             + "\nЮжный парк-Казань-Пасс: 07:35"
                             + "\nЮжный парк-Казань-Пасс: 08:49"
                             + "\nЮжный парк-Казань-Пасс: 11:41"
                             + "\nЮжный парк-Казань-Пасс: 13:56"
                             + "\nЮжный парк-Казань-Пасс: 16:34"
                             + "\nЮжный парк-Казань-Пасс: 17:36"
                             + "\nЮжный парк-Казань-Пасс: 19:05"
                             + "\nЮжный парк-Казань-Пасс: 20:41"
                             )
    elif message.text == 'Юбилейная':
        await message.answer('Все времена отправления со станции Юбилейная:'
                             + "\n Из Юбилейная в аэропорт Казань"
                             + "\nЮбилейная-аэропорт Казань: 07:03"
                             + "\nЮбилейная-аэропорт Казань: 07:47"
                             + "\nЮбилейная-аэропорт Казань: 09:40"
                             + "\nЮбилейная-аэропорт Казань: 12:45"
                             + "\nЮбилейная-аэропорт Казань: 15:28"
                             + "\nЮбилейная-аэропорт Казань: 17:05"
                             + "\nЮбилейная-аэропорт Казань: 18:30"
                             + "\nЮбилейная-аэропорт Казань: 20:05"
                             + "\n Из Юбилейная в Казань-Пасс"
                             + "\nЮбилейная-Казань-Пасс: 06:20"
                             + "\nЮбилейная-Казань-Пасс: 07:33"
                             + "\nЮбилейная-Казань-Пасс: 08:47"
                             + "\nЮбилейная-Казань-Пасс: 11:39"
                             + "\nЮбилейная-Казань-Пасс: 13:54"
                             + "\nЮбилейная-Казань-Пасс: 16:32"
                             + "\nЮбилейная-Казань-Пасс: 17:34"
                             + "\nЮбилейная-Казань-Пасс: 19:03"
                             + "\nЮбилейная-Казань-Пасс: 20:39"
                             )
    elif message.text == 'о.п. Столбище':
        await message.answer('Все времена отправления со станции о.п. Столбище:'
                             + "\n Из Столбище в аэропорт Казань"
                             + "\nСтолбище-аэропорт Казань: 07:07"
                             + "\nСтолбище-аэропорт Казань: 07:50"
                             + "\nСтолбище-аэропорт Казань: 09:43"
                             + "\nСтолбище-аэропорт Казань: 12:48"
                             + "\nСтолбище-аэропорт Казань: 15:31"
                             + "\nСтолбище-аэропорт Казань: 17:08"
                             + "\nСтолбище-аэропорт Казань: 18:33"
                             + "\nСтолбище-аэропорт Казань: 20:08"
                             + "\n Из Столбище в Казань-Пасс"
                             + "\nСтолбище-Казань-Пасс: 06:17"
                             + "\nСтолбище-Казань-Пасс: 07:30"
                             + "\nСтолбище-Казань-Пасс: 08:44"
                             + "\nСтолбище-Казань-Пасс: 11:36"
                             + "\nСтолбище-Казань-Пасс: 13:51"
                             + "\nСтолбище-Казань-Пасс: 16:29"
                             + "\nСтолбище-Казань-Пасс: 17:31"
                             + "\nСтолбище-Казань-Пасс: 19:00"
                             + "\nСтолбище-Казань-Пасс: 20:36"
                             )
    elif message.text == 'а/п Казань':
        await message.answer('Все времена отправления со станции а/п Казань:'
                             + "\n Из аэропорт Казань в Казань-Пасс"
                             + "\nаэропорт Казань-Казань-Пасс: 06:11"
                             + "\nаэропорт Казань-Казань-Пасс: 07:24"
                             + "\nаэропорт Казань-Казань-Пасс: 08:38"
                             + "\nаэропорт Казань-Казань-Пасс: 11:30"
                             + "\nаэропорт Казань-Казань-Пасс: 13:45"
                             + "\nаэропорт Казань-Казань-Пасс: 16:23"
                             + "\nаэропорт Казань-Казань-Пасс: 17:25"
                             + "\nаэропорт Казань-Казань-Пасс: 18:54"
                             + "\nаэропорт Казань-Казань-Пасс: 20:30"
                             )
    elif message.text == "Stations":
        await message.reply(
            'Вот все доступные станции:'
            + "\n1)Казань-Пасс, Привокзальная площадь, 1А, Казань"
            + "\n2)Вахитово"
            + "\n3)Тихорецкая"
            + "\n4)о.п. Березовая роща"
            + "\n5)Комбинат"
            + "\n6)о.п. Южный парк"
            + "\n7)Юбилейная"
            + "\n8)о.п. Усады"
            + "\n9)о.п. Столбище"
            + "\n10)а/п Казань, Лаишевский район, аэропорт Казань имени Габдуллы Тукая",
            reply_markup=keyboard_stations)
    else:
        await message.answer('Извините, я не понял вашего вополса😢')


executor.start_polling(dp)
