from sendFunctions import  *
from buttons_inRussian import *
from Inline_buttons import *
from botToken import bot


def call_branches(call):
    userID = call.message.chat.id
    messageID = call.message.id
    if call.data == 'worktime1':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Chilonzor filiali'
                             '\n\nπ Ish vaqtlari:\nβ°  08:00-18:00\nπ  Dushanba-Shanba\n\nπ Contact:\nπ  +998 71 276 56 66'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO1)
    if call.data == 'backTOChilanzar':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.27673611459322, longitude=69.20542894707292,
                          reply_markup=branches1)


    if call.data == 'worktime2':
        bot.delete_message(userID,messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Yakkasaroy filiali'
                             '\n\nπ Ish vaqtlari:\nβ°  09:00-19:00\nπ  Dushanba-Shanba\n\nπ Contact:\nπ  +998 71 225 64 00'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO2)
    if call.data == 'backTOYakkasaroy':
        bot.delete_message(userID,messageID)
        bot.send_location(chat_id=userID, latitude=41.28485458278078, longitude=69.25611732008919,
                          reply_markup=branches2)


    if call.data == 'worktime3':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Mustaqillik filiali'
                             '\n\nπ Ish vaqtlari:\nβ°  09:00-19:00\nπ  Dushanba-Shanba\n\nπ Contact:\nπ  +998 71 120 22 21'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO3)
    if call.data == 'backTOMustaqillik':
        bot.delete_message(userID,messageID)
        bot.send_location(chat_id=userID, latitude=41.37455400878237,longitude= 69.29578031083248,
                          reply_markup= branches3)


    if call.data == 'worktime4':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Shayxontohur filiali'
                             '\n\nπ Ish vaqtlari:\nβ°  24soat 24/7\nπ  Dushanba-Yakshanba\n\nπ Contact:\nπ  +998 71 276 56 66'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO4)
    if call.data == 'backTOShayxantohur':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.32177771439208, longitude=69.25375028331848,
                          reply_markup=branches4)

#========================================== RUS ==========================================


    if call.data == 'vremya1':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Π§ΠΈΠ»Π°Π½Π·Π°ΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                             '\n\nπ ΠΡΠ΅ΠΌΡ ΡΠ°Π±ΠΎΡΡ:\nβ°  08:00-18:00\nπ  ΠΠΎΠ½Π΅Π΄Π΅Π»ΡΠ½ΠΈΠΊ - Π‘ΡΠ±Π±ΠΎΡΠ°\n\nπ ΠΠΎΠ½ΡΠ°ΠΊΡΡ:\nπ  +998 71 276 56 66'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO1RU)
    if call.data == 'nazadvChilanzar':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.27673611459322, longitude=69.20542894707292,
                          reply_markup=branches1RU)

    if call.data == 'vremya2':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Π―ΠΊΠΊΠ°ΡΠ°ΡΠ°ΠΉΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                             '\n\nπ ΠΡΠ΅ΠΌΡ ΡΠ°Π±ΠΎΡΡ:\nβ°  09:00-19:00\nπ   ΠΠΎΠ½Π΅Π΄Π΅Π»ΡΠ½ΠΈΠΊ - Π‘ΡΠ±Π±ΠΎΡΠ°\n\nπ ΠΠΎΠ½ΡΠ°ΠΊΡΡ:\nπ  +998 71 225 64 00'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO2RU)
    if call.data == 'nazadvYakkasaroy':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.28485458278078, longitude=69.25611732008919,
                          reply_markup=branches2RU)

    if call.data == 'vremya3':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Π?Π½ΡΡΠ°Π±Π°Π΄ΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                             '\n\nπ ΠΡΠ΅ΠΌΡ ΡΠ°Π±ΠΎΡΡ:\nβ°  09:00-19:00\nπ  ΠΠΎΠ½Π΅Π΄Π΅Π»ΡΠ½ΠΈΠΊ - Π‘ΡΠ±Π±ΠΎΡΠ°\n\nπ ΠΠΎΠ½ΡΠ°ΠΊΡΡ:\nπ  +998 71 120 22 21'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO3RU)
    if call.data == 'nazadvMustaqillik':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.37455400878237, longitude=69.29578031083248,
                          reply_markup=branches3RU)

    if call.data == 'vremya4':
        bot.delete_message(userID, messageID)
        send_to_user(userID, 'π Location: RESULT SHCHOOL Π¨Π°ΠΉΡΠ°Π½ΡΠ°ΡΡΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                             '\n\nπ ΠΡΠ΅ΠΌΡ ΡΠ°Π±ΠΎΡΡ:\nβ° 24 Π§Π°ΡΠ° 24/7\nπ  ΠΠΎΠ½Π΅Π΄Π΅Π»ΡΠ½ΠΈΠΊ - ΠΠΎΡΠΊΡΠ΅ΡΠ΅Π½ΡΠ΅\n\nπ ΠΠΎΠ½ΡΠ°ΠΊΡΡ:\nπ  +998 71 276 56 66'
                             '\n\nπLink: https://t.me/resultschool\n',
                     backTO4RU)
    if call.data == 'nazadvShayxantohur':
        bot.delete_message(userID, messageID)
        bot.send_location(chat_id=userID, latitude=41.32177771439208, longitude=69.25375028331848,
                          reply_markup=branches4RU)
