import telebot
# t.me/spacelink_assistant_bot
bot = telebot.TeleBot('6462906781:AAERYLFxbDrfDAoEJ0MNuL3MV2lNDegc06M')
@bot.message_handler(content_types=['text'])
def get_text_massage(message):
  if message.text == "/schedule":
    bot.send_message(message.from_user.id, "Кварк (Команда: SpaceLink/Atom, Тестовая ракета, РД1-100-0): Начало апреля 2025")
    bot.send_message(message.from_user.id, "Атом 3Е (Команда: МДП-Atom, Реактивное Движение, РДК-2000): Начало мая 2025")
    bot.send_message(message.from_user.id, "Атом 3 (Команда: МДП-Atom, ВИШ Кансат, РД1-300-0): Июль 2025")
    bot.send_message(message.from_user.id, "[название] (Команда: R&A, ВИШ Кансат, РД1-100, Запуск с самолета): Июль 2025")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Я секретарь. Я могу помочь Вам найти информацию о SpaceLink, например расписание пусков /schedule.\n\n/disclaimer")
  elif message.text == "/start":
    bot.send_message(message.from_user.id, "Здравствуйте! Я секретарь.\nЯ могу помочь Вам найти информацию о SpaceLink.\n\n/help\n/disclaimer")
  elif message.text == "/disclaimer":
    bot.send_message(message.from_user.id, "Ракетостроение — сложная и опасная область, требующая знаний и строгого соблюдения безопасности. Мы имеем опыт и работаем с экспертами, и не рекомендуем повторять показанное.\n\nВсе действия вы совершаете на свой страх и риск. Соблюдайте законы и технику безопасности!")
  elif message.text == "/social":
    bot.send_message(message.from_user.id, "Телеграм канал: t.me/AndySpaceCompany\nYouTube канал: www.youtube.com/@SpaceLinkCommercial")
  else:
    bot.send_message(message.from_user.id, "Я Вас не понимаю. Напишите /help.")

bot.polling(none_stop=True, interval=2)
