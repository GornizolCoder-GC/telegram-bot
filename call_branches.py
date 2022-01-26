from sendFunctions import  *
from buttons_inRussian import *
from Inline_buttons import *
from botToken import bot


def call_branches(call):
    userID = call.message.chat.id
    messageID = call.message.id
    if call.data == 'worktime1':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Chilonzor filiali'
                             '\n\n📌 Ish vaqtlari:\n⏰  08:00-18:00\n📆  Dushanba-Shanba\n\n📌 Contact:\n📞  +998 71 276 56 66'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO1)
    if call.data == 'backTOChilanzar':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.27673611459322, longitude=69.20542894707292,
                          reply_markup=branches1)


    if call.data == 'worktime2':
        bot.delete_message(userID,messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Yakkasaroy filiali'
                             '\n\n📌 Ish vaqtlari:\n⏰  09:00-19:00\n📆  Dushanba-Shanba\n\n📌 Contact:\n📞  +998 71 225 64 00'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO2)
    if call.data == 'backTOYakkasaroy':
        bot.delete_message(userID,messageID)
        bot.send_location(chat_id=userID, latitude=41.28485458278078, longitude=69.25611732008919,
                          reply_markup=branches2)


    if call.data == 'worktime3':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Mustaqillik filiali'
                             '\n\n📌 Ish vaqtlari:\n⏰  09:00-19:00\n📆  Dushanba-Shanba\n\n📌 Contact:\n📞  +998 71 120 22 21'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO3)
    if call.data == 'backTOMustaqillik':
        bot.delete_message(userID,messageID)
        bot.send_location(chat_id=userID, latitude=41.37455400878237,longitude= 69.29578031083248,
                          reply_markup= branches3)


    if call.data == 'worktime4':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Shayxontohur filiali'
                             '\n\n📌 Ish vaqtlari:\n⏰  24soat 24/7\n📆  Dushanba-Yakshanba\n\n📌 Contact:\n📞  +998 71 276 56 66'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO4)
    if call.data == 'backTOShayxantohur':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.32177771439208, longitude=69.25375028331848,
                          reply_markup=branches4)

#========================================== RUS ==========================================


    if call.data == 'vremya1':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Чиланзарский филиал'
                             '\n\n📌 Время работы:\n⏰  08:00-18:00\n📆  Понедельник - Суббота\n\n📌 Контакты:\n📞  +998 71 276 56 66'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO1RU)
    if call.data == 'nazadvChilanzar':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.27673611459322, longitude=69.20542894707292,
                          reply_markup=branches1RU)

    if call.data == 'vremya2':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Яккасарайский филиал'
                             '\n\n📌 Время работы:\n⏰  09:00-19:00\n📆   Понедельник - Суббота\n\n📌 Контакты:\n📞  +998 71 225 64 00'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO2RU)
    if call.data == 'nazadvYakkasaroy':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.28485458278078, longitude=69.25611732008919,
                          reply_markup=branches2RU)

    if call.data == 'vremya3':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Юнусабадский филиал'
                             '\n\n📌 Время работы:\n⏰  09:00-19:00\n📆  Понедельник - Суббота\n\n📌 Контакты:\n📞  +998 71 120 22 21'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO3RU)
    if call.data == 'nazadvMustaqillik':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.37455400878237, longitude=69.29578031083248,
                          reply_markup=branches3RU)

    if call.data == 'vremya4':
        bot.delete_message(userID, messageID)
        send_to_user(userID, '📍 Location: RESULT SHCHOOL Шайхантахурский филиал'
                             '\n\n📌 Время работы:\n⏰ 24 Часа 24/7\n📆  Понедельник - Воскресенье\n\n📌 Контакты:\n📞  +998 71 276 56 66'
                             '\n\n👉Link: https://t.me/resultschool\n',
                     backTO4RU)
    if call.data == 'nazadvShayxantohur':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.32177771439208, longitude=69.25375028331848,
                          reply_markup=branches4RU)
