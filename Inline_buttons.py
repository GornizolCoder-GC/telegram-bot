from telebot import types
from buttons_inRussian import mainRU

##################################################################################

#---------------------- Tilni tanlash ----------------------#

inlineButtonLAN = types.InlineKeyboardMarkup()
itemUZ = types.InlineKeyboardButton(text='🇺🇿 Uzbek', callback_data='uz')
itemRU = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='ru')

inlineButtonLAN.add(itemUZ, itemRU)

#----------------------QAYTA Tilni tanlash ----------------------#

inlineButtonLAN2 = types.InlineKeyboardMarkup()
itemUZ = types.InlineKeyboardButton(text='🇺🇿 O`zbek', callback_data='menu')
itemRU = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='mainmenu')

inlineButtonLAN2.add(itemUZ, itemRU)
##################################################################################

#---------------------- So`rovnoma ----------------------#

#>>>>>>>>>>>>>>>> I1-savol
inlineButtonQA = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='👨‍🎓👩‍🎓 Talaba', callback_data='T')
item2 = types.InlineKeyboardButton(text='👨‍👩‍👧‍👦 Ota-Ona', callback_data='family')

inlineButtonQA.add(item1, item2)


#>>>>>>>>>>>>>>>> I2-savol
inlineButtonQA1 = types.InlineKeyboardMarkup()
inlineButtonQA1.add(types.InlineKeyboardButton(text='✅ HA', callback_data='yes'), types.InlineKeyboardButton(text='❌ YO`Q', callback_data='no'))

#>>>>>>>>>>>>>>>> SAVOLLAR UCHUN JOY SHU YERDA <<<<<<<<<<<<<<<<




#---------------------- BOSHQARUVCHI KNOPKALAR ----------------------#

ManageButtonCourse = types.InlineKeyboardMarkup()
main = types.InlineKeyboardButton(text='🔰 Bosh Menyu', callback_data='menu')
back = types.InlineKeyboardButton(text='🔙 Orqaga', callback_data='backTOmainMENU')
InlineURL = types.InlineKeyboardButton(text='ResultUZ School courses', url='https://www.result.uz/index.html#two')
ManageButtonCourse.add(InlineURL)
ManageButtonCourse.add(main,back)

ManageButtonMentors = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton(text='🔙 Orqaga', callback_data='backTOmentors')
InlineURLmentors = types.InlineKeyboardButton(text='Batafsil ma`lumot uchun', url='https://www.result.uz/index.html#three')
ManageButtonMentors.add(InlineURLmentors)
ManageButtonMentors.add(main,back1)

##################################################################################
#---------------------- Messenjerlarga KNOPKALINKLAR ----------------------#

InlineURLMessengers = types.InlineKeyboardMarkup()
InlineURLMessengers.add(types.InlineKeyboardButton(text='🔗 Telegram Link', url='https://t.me/ResultUz'))
InlineURLMessengers.add(types.InlineKeyboardButton(text='🔗 Instagram Link', url='https://www.instagram.com/p/CSYuiXID9E_/?utm_medium=copy_link'))
InlineURLMessengers.add(main)

InlineURLMessengersRU = types.InlineKeyboardMarkup()
InlineURLMessengersRU.add(types.InlineKeyboardButton(text='🔗 Telegram Link', url='https://t.me/ResultUz'))
InlineURLMessengersRU.add(types.InlineKeyboardButton(text='🔗 Instagram Link', url='https://www.instagram.com/p/CSYuiXID9E_/?utm_medium=copy_link'))
InlineURLMessengersRU.add(mainRU)

##################################################################################

#---------------------- Filial - XARITA KNOPKALINKLAR ----------------------#

branches1 = types.InlineKeyboardMarkup()
branches2 = types.InlineKeyboardMarkup()
branches3 = types.InlineKeyboardMarkup()
branches4 = types.InlineKeyboardMarkup()

backbranch = types.InlineKeyboardButton(text='📍 Filiallar', callback_data='backTObranches')
backTO1 = types.InlineKeyboardMarkup()
backTO2 = types.InlineKeyboardMarkup()
backTO3 = types.InlineKeyboardMarkup()
backTO4 = types.InlineKeyboardMarkup()
backTO1.add(types.InlineKeyboardButton(text='🔙 Ortga qaytish', callback_data='backTOChilanzar'))
backTO2.add(types.InlineKeyboardButton(text='🔙 Ortga qaytish', callback_data='backTOYakkasaroy'))
backTO3.add(types.InlineKeyboardButton(text='🔙 Ortga qaytish', callback_data='backTOMustaqillik'))
backTO4.add(types.InlineKeyboardButton(text='🔙 Ortga qaytish', callback_data='backTOShayxantohur'))

InlineURLbranche1 = types.InlineKeyboardButton(text='🗺 xaritadan qidirish', url='https://goo.gl/maps/rTJjh3GbhATADhGM9')
workTIME1 = types.InlineKeyboardButton(text='⏰ Ish vaqtlar', callback_data='worktime1')
branches1.add(InlineURLbranche1)
branches1.add(workTIME1, backbranch)
branches1.add(main)

InlineURLbranche2 = types.InlineKeyboardButton(text='🗺 xaritadan qidirish', url='https://goo.gl/maps/4g9ThAtNqhBHtqXN8')
workTIME2 = types.InlineKeyboardButton(text='⏰ Ish vaqtlar', callback_data='worktime2')
branches2.add(InlineURLbranche2)
branches2.add(workTIME2, backbranch)
branches2.add(main)

InlineURLbranche3 = types.InlineKeyboardButton(text='🗺 xaritadan qidirish', url='https://goo.gl/maps/UpDEUqxk7NTLbnYRA')
workTIME3 = types.InlineKeyboardButton(text='⏰ Ish vaqtlar', callback_data='worktime3')
branches3.add(InlineURLbranche3)
branches3.add(workTIME3, backbranch)
branches3.add(main)

InlineURLbranche4 = types.InlineKeyboardButton(text='🗺 xaritadan qidirish', url='https://goo.gl/maps/DNoebm8T2qJkBA287')
workTIME4 = types.InlineKeyboardButton(text='⏰ Ish vaqtlar', callback_data='worktime4')
branches4.add(InlineURLbranche4)
branches4.add(workTIME4, backbranch)
branches4.add(main)

#---------------------- inline_KURSLAR ----------------------#

keyboardCourse = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='❕ English Fundamentals', callback_data='course1')
item2 = types.InlineKeyboardButton(text='❕ Math in English', callback_data='course5')
item3 = types.InlineKeyboardButton(text='❕ IELTS 7+', callback_data='course3')
item4 = types.InlineKeyboardButton(text='❕ IELTS FOCUS', callback_data='course4')
item5 = types.InlineKeyboardButton(text='❕ IELTS Master', callback_data='course2')
keyboardCourse.add(item1)
keyboardCourse.add(item2, item3)
keyboardCourse.add(item4, item5)
keyboardCourse.add(InlineURL)
keyboardCourse.add(main)


#---------------------- inline_MENTORLAR ----------------------#

keyboard_techers = types.InlineKeyboardMarkup()
t1 = types.InlineKeyboardButton(text='1', callback_data='t1')
t2 = types.InlineKeyboardButton(text='2', callback_data='t2')
t3 = types.InlineKeyboardButton(text='3', callback_data='t3')
t4 = types.InlineKeyboardButton(text='4', callback_data='t4')
t5 = types.InlineKeyboardButton(text='5', callback_data='t5')
t6 = types.InlineKeyboardButton(text='6', callback_data='t6')
t7 = types.InlineKeyboardButton(text='7', callback_data='t7')
t8 = types.InlineKeyboardButton(text='8', callback_data='t8')
t9 = types.InlineKeyboardButton(text='9', callback_data='t9')

keyboard_techers.add(t1,t2,t3)
keyboard_techers.add(t4,t5,t6)
keyboard_techers.add(t7,t8,t9)
keyboard_techers.add(InlineURLmentors)
keyboard_techers.add(main)

#---------------------- Level Test ----------------------#

levelTEST = types.InlineKeyboardMarkup()
levelTEST.add(types.InlineKeyboardButton(text='👉 🔺level test🔻 👈',
                                         url='https://docs.google.com/forms/d/e/1FAIpQLSd2JBqPQD9caRlxNmVF9VvsMC9aYk6rFtG4vHSFZNcGPIBOLw/viewform'))
levelTEST.add(main)

#---------------------- HELP Command ----------------------#

helpCOMM = types.InlineKeyboardMarkup()
helpCOMM.add(main)