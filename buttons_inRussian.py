from telebot import types

##################################################################################

#---------------------- So`rovnoma ----------------------#

#>>>>>>>>>>>>>>>> I1-savol
inlineButtonQARU = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='👨‍🎓👩‍🎓  Студент', callback_data='stu')
item2 = types.InlineKeyboardButton(text='👨‍👩‍👧‍👦  Родитель', callback_data='parent')

inlineButtonQARU.add(item1, item2)


#>>>>>>>>>>>>>>>> I2-savol
inlineButtonQA1RU = types.InlineKeyboardMarkup()
inlineButtonQA1RU.add(types.InlineKeyboardButton(text='✅Да', callback_data='da'), types.InlineKeyboardButton(text='❌ Нет', callback_data='net'))

#>>>>>>>>>>>>>>>> SAVOLLAR UCHUN JOY SHU YERDA <<<<<<<<<<<<<<<<



##################################################################################

#---------------------- BOSHQARUVCHI KNOPKALAR ----------------------#

ManageButtonCourseRU = types.InlineKeyboardMarkup()
mainRU = types.InlineKeyboardButton(text='🔰 Главное меню', callback_data='mainmenu')
backRU = types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazdvmenyu')
InlineURL = types.InlineKeyboardButton(text='ResultUZ School courses', url='https://www.result.uz/index.html#two')
ManageButtonCourseRU.add(InlineURL)
ManageButtonCourseRU.add(mainRU,backRU)

ManageButtonMentorsRU = types.InlineKeyboardMarkup()
back1RU = types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazadvmentors')
InlineURLmentors = types.InlineKeyboardButton(text='Подробное информация', url='https://www.result.uz/index.html#three')
ManageButtonMentorsRU.add(InlineURLmentors)
ManageButtonMentorsRU.add(mainRU,back1RU)


##################################################################################

#---------------------- Filial - XARITA KNOPKALINKLAR ----------------------#

branches1RU = types.InlineKeyboardMarkup()
branches2RU = types.InlineKeyboardMarkup()
branches3RU = types.InlineKeyboardMarkup()
branches4RU = types.InlineKeyboardMarkup()

backbranchRU = types.InlineKeyboardButton(text='📍 Наши филиалы', callback_data='nazadvbrench')
backTO1RU = types.InlineKeyboardMarkup()
backTO2RU = types.InlineKeyboardMarkup()
backTO3RU = types.InlineKeyboardMarkup()
backTO4RU = types.InlineKeyboardMarkup()
backTO1RU.add(types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazadvChilanzar'))
backTO2RU.add(types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazadvYakkasaroy'))
backTO3RU.add(types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazadvMustaqillik'))
backTO4RU.add(types.InlineKeyboardButton(text='🔙 Назад', callback_data='nazadvShayxantohur'))

InlineURLbranche1 = types.InlineKeyboardButton(text='🗺 Поиск в карте', url='https://goo.gl/maps/rTJjh3GbhATADhGM9')
workTIME1RU = types.InlineKeyboardButton(text='⏰ Время работы', callback_data='vremya1')
branches1RU.add(InlineURLbranche1)
branches1RU.add(workTIME1RU, backbranchRU)
branches1RU.add(mainRU)

InlineURLbranche2 = types.InlineKeyboardButton(text='🗺 Поиск в карте', url='https://goo.gl/maps/4g9ThAtNqhBHtqXN8')
workTIME2RU = types.InlineKeyboardButton(text='⏰ Время работы', callback_data='vremya2')
branches2RU.add(InlineURLbranche2)
branches2RU.add(workTIME2RU, backbranchRU)
branches2RU.add(mainRU)

InlineURLbranche3 = types.InlineKeyboardButton(text='🗺 Поиск в карте', url='https://goo.gl/maps/UpDEUqxk7NTLbnYRA')
workTIME3RU = types.InlineKeyboardButton(text='⏰ Время работы', callback_data='vremya3')
branches3RU.add(InlineURLbranche3)
branches3RU.add(workTIME3RU, backbranchRU)
branches3RU.add(mainRU)

InlineURLbranche4 = types.InlineKeyboardButton(text='🗺 Поиск в карте', url='https://goo.gl/maps/DNoebm8T2qJkBA287')
workTIME4RU = types.InlineKeyboardButton(text='⏰ Время работы', callback_data='vremya4')
branches4RU.add(InlineURLbranche4)
branches4RU.add(workTIME4RU, backbranchRU)
branches4RU.add(mainRU)

#---------------------- inline_KURSLAR ----------------------#

keyboardCourseRU = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='❕ English Fundamentals', callback_data='kurs1')
item2 = types.InlineKeyboardButton(text='❕ Math in English', callback_data='kurs5')
item3 = types.InlineKeyboardButton(text='❕ IELTS 7+', callback_data='kurs3')
item4 = types.InlineKeyboardButton(text='❕ IELTS FOCUS', callback_data='kurs4')
item5 = types.InlineKeyboardButton(text='❕ IELTS Master', callback_data='kurs2')
keyboardCourseRU.add(item1)
keyboardCourseRU.add(item2, item3)
keyboardCourseRU.add(item4, item5)
keyboardCourseRU.add(InlineURL)


#---------------------- inline_MENTORLAR ----------------------#

keyboard_techersRU = types.InlineKeyboardMarkup()
t1 = types.InlineKeyboardButton(text='1', callback_data='f1')
t2 = types.InlineKeyboardButton(text='2', callback_data='f2')
t3 = types.InlineKeyboardButton(text='3', callback_data='f3')
t4 = types.InlineKeyboardButton(text='4', callback_data='f4')
t5 = types.InlineKeyboardButton(text='5', callback_data='f5')
t6 = types.InlineKeyboardButton(text='6', callback_data='f6')
t7 = types.InlineKeyboardButton(text='7', callback_data='f7')
t8 = types.InlineKeyboardButton(text='8', callback_data='f8')
t9 = types.InlineKeyboardButton(text='9', callback_data='f9')

keyboard_techersRU.add(t1,t2,t3)
keyboard_techersRU.add(t4,t5,t6)
keyboard_techersRU.add(t7,t8,t9)
keyboard_techersRU.add(InlineURLmentors)
keyboard_techersRU.add(mainRU)

#---------------------- Level Test ----------------------#

TESTRU = types.InlineKeyboardMarkup()
TESTRU.add(types.InlineKeyboardButton(text='👉 🔺level test🔻 👈',
                                         url='https://docs.google.com/forms/d/e/1FAIpQLSd2JBqPQD9caRlxNmVF9VvsMC9aYk6rFtG4vHSFZNcGPIBOLw/viewform'))
TESTRU.add(mainRU)