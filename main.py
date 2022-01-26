from AQ import aq
from sendFunctions import *
from call_mentors import call_mentors
from call_courses import call_courses
from call_branches import call_branches
# ----------------------------------------------------
from Inline_buttons import *    # inline Buttons UZ
from buttons_inRussian import *    # inline Buttons RU
# ----------------------------------------------------
from Reply_buttons import *     # reply Buttons
# ----------------------------------------------------




#########################################################################################################
#UZB
def levelTest(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id,
                     text='📣 RESULT bilan ingliz tilida o`z bilim darajangizni tekshirib ko`ring!'
                          '\n\n🏁 Level Test'
                          '\n\n📌 Jami savollar soni: 50 ta'
                          '\n⏰ Vaqt limiti: ♾'
                          '\n✅ Tog`ri javob - 1 ball'
                          '\n❌ Noto`g`ri javob - 0 ball'
                          '\n\n🔥🔥🔥 Kutmang, hoziroq boshlang!😎😎 Pastdagi "👉🔺level test🔻👈" '
                          'tugmachani bosing va o`z bilimlaringizni sinab ko`ring!'
                          '\n\n🎯ResultUZ: "From NO to YES"', reply_markup=levelTEST)
def mainCOURSE(message):

    send_to_user(message.chat.id, 'Result O`quv marazi kurslar:\n'
                         '\n ✅ English Fundamentals'
                         '\n ✅ IELTS Master'
                         '\n ✅ IELTS 7+'
                         '\n ✅ IELTS FOCUS'
                         '\n ✅ Math in English'
                         '\n Kurslar haqida batafsil ma`lumotlar uchun link 👇'
                         '\n https://www.result.uz/index.html#two', keyboardCourse)

def mainBranches(message):

    send_to_user(message.chat.id, 'Quyida RESULT SCHOOL filiallari haqida bilib '
                         'olishingiz mumkin. Kerakli filialni tanlang: ',
                 branch
                 )

def mentors(message):

    send_to_user(message.chat.id, '💎 Result O`quv marazi malakali mutaxasislari ro`yhati:'
                                   '\n\n1️⃣ - Harry Tompson \nIELTS Instructor\n'
                                   '\n2️⃣ - Mustafo Zafarovich \nIELTS Instructor\n'
                                   '\n3️⃣ - Rustam Umarovich \nLanguage Instructor\n'
                                   '\n4️⃣ - Abdurakhim Jalilov \nTESOL Certified Teacher\n'
                                   '\n5️⃣ - Sharof Rashidov \nIELTS Instructor\n'
                                   '\n6️⃣ - Aziz Normurodov \nLanguage Instructor\n'
                                   '\n7️⃣ - Bakhodir Abdullayev \nLanguage Instructor\n'
                                   '\n8️⃣ - Iskandarbek Kamoliddinov \nIELTS Instructor\n'
                                   '\n9️⃣ - Nasibaxon Raupova \nLanguage Instructor\n'
                                  '\n📣🤔 O`zingizni qiziqtirgan mentorlarni tanlang va ular'
                                  ' haqida ma`lumotlarga ega bo`ling!', keyboard_techers)

def contact(message):
    send_to_photo(message.chat.id, open('Contact/contact-us.jpg', 'rb'),
                  '📞 Kontaktlar | Telegram | Instagram'
                  '\n\n 🏛 RESULT SHCHOOL Chilonzor filiali'
                  '\n ☎ Tel: +998 71 276 56 66'
                  '\n\n 🏛 RESULT SHCHOOL Yakkasaroy filiali'
                  '\n ☎ Tel: +998 71 225 64 00'
                  '\n\n 🏛 RESULT SHCHOOL Mustaqillik filiali'
                  '\n ☎ Tel: +998 71 120 22 21'
                  '\n\n 🏛 RESULT SHCHOOL Shayxontohur filiali'
                  '\n ☎ Tel: +998 71 276 56 66'
                  '\n\n👉Link: https://t.me/resultschool\n', InlineURLMessengers)

def settings(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text='Muloqot tilini o`zgartirish:',
                     reply_markup=inlineButtonLAN2)

#########################################################################################################
#########################################################################################################
#RUS
def levelTestRU(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id,
                     text='📣 Посмотрите, как измерить свой уровень знания английского языка с помощью RESULT!'
                          '\n\n🏁 Узнать свой уровень знаний 🏁'
                          '\n\n📌 Всего вопросов: 50'
                          '\n⏰ Лимит времени: ♾'
                          '\n✅ Правильный ответ - 1 балл'
                          '\n❌ Неверный ответ - 0 баллов'
                          '\n\n🔥🔥🔥 Не ждите, начните сейчас! 😎😎 Нажмите кнопку'
                          ' "👉🔺level test🔻👈" ниже и проверьте свои знания!'
                          '\n\n🎯ResultUZ: "From NO to YES"', reply_markup=TESTRU)

def mainCOURSERU(message):
    send_to_user(message.chat.id, 'Курсы учебного центра Result:\n'
                                  '\n ✅ English Fundamentals'
                                  '\n ✅ IELTS Master'
                                  '\n ✅ IELTS 7+'
                                  '\n ✅ IELTS FOCUS'
                                  '\n ✅ Math in English'
                                  '\n Линк для подробной информации о курсах 👇'
                                  '\n https://www.result.uz/index.html#two', keyboardCourseRU)


def mainBranchesRU(message):
    send_to_user(message.chat.id, 'Внизу подробное информация о наших  филиалах , Выберите нужный вам филиал.',
                 branchRU
                 )

def mentorsRU(message):
    send_to_user(message.chat.id, '💎 Список квалифицированных специалистов учебного заведения Result:'
                                  '\n\n1️⃣ - Harry Tompson \nIELTS Instructor\n'
                                  '\n2️⃣ - Mustafo Zafarovich \nIELTS Instructor\n'
                                  '\n3️⃣ - Rustam Umarovich \nLanguage Instructor\n'
                                  '\n4️⃣ - Abdurakhim Jalilov \nTESOL Certified Teacher\n'
                                  '\n5️⃣ - Sharof Rashidov \nIELTS Instructor\n'
                                  '\n6️⃣ - Aziz Normurodov \nLanguage Instructor\n'
                                  '\n7️⃣ - Bakhodir Abdullayev \nLanguage Instructor\n'
                                  '\n8️⃣ - Iskandarbek Kamoliddinov \nIELTS Instructor\n'
                                  '\n9️⃣ - Nasibaxon Raupova \nLanguage Instructor\n'
                                  '\n📣🤔 Выберите наставников, которые вам интересны'
                                  ' И узнайте о них больше!!', keyboard_techersRU)

def contactRU(message):
    send_to_photo(message.chat.id, open('Contact/contact-us.jpg', 'rb'),
                  '📞 Контакты| Telegram | Instagram'
                  '\n\n 🏛 RESULT SHCHOOL Чиланзарский филиал'
                  '\n ☎ Tel: +998 71 276 56 66'
                  '\n\n 🏛 RESULT SHCHOOL Яккасарайский филиал'
                  '\n ☎ Tel: +998 71 225 64 00'
                  '\n\n 🏛 RESULT SHCHOOL Юнусабадский филиал'
                  '\n ☎ Tel: +998 71 120 22 21'
                  '\n\n 🏛 RESULT SHCHOOL Шайхантахурский филиал'
                  '\n ☎ Tel: +998 71 276 56 66'
                  '\n\n👉Link: https://t.me/resultschool\n', InlineURLMessengersRU)


def settingsRU(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text='Измените язык общения:',
                     reply_markup=inlineButtonLAN2)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    userId = message.chat.id
    text1 = '🇺🇿 Assalomu alaykum! \nResultUZ Telegram botga xush kelibsiz! \nMuloqot tilini tanlang:' \
            '\n\n🇷🇺 Здравствуйте ! \nДобро пожаловать в телеграм бот Result \nПожалуйста выберите язык для общения  '
    text2 = '⁉️ResultUZ botdan foydalanish yo`riqnomasi:' \
            '\n🇺🇿 O`zbek - o`zbek tili' \
            '\n\nBot komandalari:' \
            '\n /start komandasi - botni ishga tushirish' \
            '\n /help komandasi - botni ishlatish yo`riqnomasi' \
            '\n\nBot menyu:' \
            '\n 🏁 Level Test - Darajali test savollar' \
            '\n 📝 Kurslar - ResultUZ kurslari' \
            '\n 🎓 Mentorlar - ResultUZ o`qituvchilar' \
            '\n 📍 Filiallar - ResultUZ filiallari' \
            '\n 📞 Kontaktlar - ResultUZ bilan aloqa' \
            '\n ⚙ Sozlamalar - Tilni o`zgartirish'\
            '\n\n⁉️Инструкция по использованию бота ResultUZ:' \
            '\n🇷🇺 Русский - Русский язык' \
            '\n\nКоманды бота:' \
            '\n /start command - запустить бота' \
            '\n /help command - инструкция по использованию бота' \
            '\n\nМеню бота:' \
            '\n 🏁 Узнать свой уровень знаний 🏁 - Вопросы для проверки уровня' \
            '\n 📝 Наши курсы - ResultUZ курсы' \
            '\n 🎓 Наши Менторы - ResultUZ учителя' \
            '\n 📍 Наши филиалы - ResultUZ филиалы' \
            '\n 📞 Наши контактыr - Связаться с ResultUZ' \
            '\n ⚙ Настройки - Изменить язык'
    if message.text == '/start':
        send_to_user(userId, text1, inlineButtonLAN)
    elif message.text == '/help':
        bot.send_message(chat_id=userId,text=text2)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    userID = call.message.chat.id
    messageID = call.message.id

    aq(call)
    call_mentors(call)
    call_courses(call)
    call_branches(call)


    if call.data == 'menu':
        send_to_user(userID,'<< BOSH MENYU >>', menyu)

    if call.data == 'backTOmainMENU':
        bot.delete_message(userID, messageID)
        mainCOURSE(call.message)

    if call.data == 'backTOmentors':
        bot.delete_message(userID,messageID)
        mentors(call.message)

    if call.data == 'backTObranches':
        bot.delete_message(userID,messageID)
        mainBranches(call.message)
    #----------------------------- RUS ------------------------------------

    if call.data == 'mainmenu':
        send_to_user(userID, '<< Главное меню >>', menyuRU)

    if call.data == 'nazdvmenyu':
        bot.delete_message(userID, messageID)
        mainCOURSERU(call.message)

    if call.data == 'nazadvmentors':
        bot.delete_message(userID, messageID)
        mentorsRU(call.message)

    if call.data == 'nazadvbrench':
        bot.delete_message(userID, messageID)
        mainBranchesRU(call.message)


@bot.message_handler(content_types=['text'])
def step1(message):
    userId = message.chat.id
    messageId = message.id

    # ****************************************************************** Kurslar ******************************************************************

    if message.text == '🏁 Level Test':
        levelTest(message)

    elif message.text == '📝 Kurslar':
        mainCOURSE(message)

    elif message.text == '🎓 Mentorlar':
        mentors(message)

    elif message.text == '📍 Filiallar':
        mainBranches(message)

    elif message.text == '📞 Kontaktlar':
        contact(message)

    elif message.text == 'Chilonzor filiali':
        send_to_location(userId, 41.27673611459322, 69.20542894707292, message.id, branches1)
        # send_to_photo(userId, open('branchs/brchilanzar.jpg', 'rb'), )

    elif message.text == 'Yakkasaroy filiali':
        send_to_location(userId, 41.28485458278078, 69.25611732008919, message.id, branches2)
        # send_to_photo(userId, open('branchs/bryakkasaroy.jpg', 'rb'),)

    elif message.text == 'Mustaqillik filiali':
        # send_to_photo(userId, open('branchs/brmustaqillik.jpg','rb'),...)
        send_to_location(userId, 41.37455400878237, 69.29578031083248, message.id, branches3)

    elif message.text == 'Shayxontohur filiali':
        send_to_location(userId, 41.32177771439208, 69.25375028331848, message.id, branches4)
        # send_to_photo(userId, open('branchs/brshayhontohur.jpg', 'rb'),)

    elif message.text == '🔙 Orqaga':
        send_to_user(userId, '<< BOSH MENYU >>', menyu)

    elif message.text == '⚙ Sozlamalar':
        settings(message)

#====================================================== RUS ======================================================

    elif message.text == '🏁 Узнать свой уровень знаний 🏁':
        levelTestRU(message)

    elif message.text == '📝 Наши курсы':
        mainCOURSERU(message)

    elif message.text == '🎓 Наши Менторы':
        mentorsRU(message)

    elif message.text == '📍 Наши филиалы':
        mainBranchesRU(message)

    elif message.text == '📞 Наши контакты':
        contactRU(message)

    elif message.text == 'Чиланзарский филиал':
        send_to_location(message.chat.id, 41.27673611459322, 69.20542894707292, message.id, branches1RU)
        # send_to_photo(userId, open('branchs/brchilanzar.jpg', 'rb'), )

    elif message.text == 'Яккасарайский филиал':
        send_to_location(message.chat.id, 41.28485458278078, 69.25611732008919, message.id, branches2RU)
        # send_to_photo(userId, open('branchs/bryakkasaroy.jpg', 'rb'),)

    elif message.text == 'Юнусабадский филиал':
        # send_to_photo(userId, open('branchs/brmustaqillik.jpg','rb'),...)
        send_to_location(message.chat.id, 41.37455400878237, 69.29578031083248, message.id, branches3RU)

    elif message.text == 'Шайхантахурский филиал':
        send_to_location(message.chat.id, 41.32177771439208, 69.25375028331848, message.id, branches4RU)
        # send_to_photo(userId, open('branchs/brshayhontohur.jpg', 'rb'),)

    elif message.text == '🔙 Назад':
        send_to_user(message.chat.id, '<< Главное меню >>', menyuRU)

    elif message.text == '⚙ Настройки':
        settingsRU(message)

    else:
        bot.reply_to(message, message.text)  # reply rejimida javob qaytaradi

print('The telegram bot is working :)')

bot.polling(none_stop=True)
