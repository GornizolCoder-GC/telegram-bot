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
                     text='π£ RESULT bilan ingliz tilida o`z bilim darajangizni tekshirib ko`ring!'
                          '\n\nπ Level Test'
                          '\n\nπ Jami savollar soni: 50 ta'
                          '\nβ° Vaqt limiti: βΎ'
                          '\nβ Tog`ri javob - 1 ball'
                          '\nβ Noto`g`ri javob - 0 ball'
                          '\n\nπ₯π₯π₯ Kutmang, hoziroq boshlang!ππ Pastdagi "ππΊlevel testπ»π" '
                          'tugmachani bosing va o`z bilimlaringizni sinab ko`ring!'
                          '\n\nπ―ResultUZ: "From NO to YES"', reply_markup=levelTEST)
def mainCOURSE(message):

    send_to_user(message.chat.id, 'Result O`quv marazi kurslar:\n'
                         '\n β English Fundamentals'
                         '\n β IELTS Master'
                         '\n β IELTS 7+'
                         '\n β IELTS FOCUS'
                         '\n β Math in English'
                         '\n Kurslar haqida batafsil ma`lumotlar uchun link π'
                         '\n https://www.result.uz/index.html#two', keyboardCourse)

def mainBranches(message):

    send_to_user(message.chat.id, 'Quyida RESULT SCHOOL filiallari haqida bilib '
                         'olishingiz mumkin. Kerakli filialni tanlang: ',
                 branch
                 )

def mentors(message):

    send_to_user(message.chat.id, 'π Result O`quv marazi malakali mutaxasislari ro`yhati:'
                                   '\n\n1οΈβ£ - Harry Tompson \nIELTS Instructor\n'
                                   '\n2οΈβ£ - Mustafo Zafarovich \nIELTS Instructor\n'
                                   '\n3οΈβ£ - Rustam Umarovich \nLanguage Instructor\n'
                                   '\n4οΈβ£ - Abdurakhim Jalilov \nTESOL Certified Teacher\n'
                                   '\n5οΈβ£ - Sharof Rashidov \nIELTS Instructor\n'
                                   '\n6οΈβ£ - Aziz Normurodov \nLanguage Instructor\n'
                                   '\n7οΈβ£ - Bakhodir Abdullayev \nLanguage Instructor\n'
                                   '\n8οΈβ£ - Iskandarbek Kamoliddinov \nIELTS Instructor\n'
                                   '\n9οΈβ£ - Nasibaxon Raupova \nLanguage Instructor\n'
                                  '\nπ£π€ O`zingizni qiziqtirgan mentorlarni tanlang va ular'
                                  ' haqida ma`lumotlarga ega bo`ling!', keyboard_techers)

def contact(message):
    send_to_photo(message.chat.id, open('Contact/contact-us.jpg', 'rb'),
                  'π Kontaktlar | Telegram | Instagram'
                  '\n\n π RESULT SHCHOOL Chilonzor filiali'
                  '\n β Tel: +998 71 276 56 66'
                  '\n\n π RESULT SHCHOOL Yakkasaroy filiali'
                  '\n β Tel: +998 71 225 64 00'
                  '\n\n π RESULT SHCHOOL Mustaqillik filiali'
                  '\n β Tel: +998 71 120 22 21'
                  '\n\n π RESULT SHCHOOL Shayxontohur filiali'
                  '\n β Tel: +998 71 276 56 66'
                  '\n\nπLink: https://t.me/resultschool\n', InlineURLMessengers)

def settings(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text='Muloqot tilini o`zgartirish:',
                     reply_markup=inlineButtonLAN2)

#########################################################################################################
#########################################################################################################
#RUS
def levelTestRU(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id,
                     text='π£ ΠΠΎΡΠΌΠΎΡΡΠΈΡΠ΅, ΠΊΠ°ΠΊ ΠΈΠ·ΠΌΠ΅ΡΠΈΡΡ ΡΠ²ΠΎΠΉ ΡΡΠΎΠ²Π΅Π½Ρ Π·Π½Π°Π½ΠΈΡ Π°Π½Π³Π»ΠΈΠΉΡΠΊΠΎΠ³ΠΎ ΡΠ·ΡΠΊΠ° Ρ ΠΏΠΎΠΌΠΎΡΡΡ RESULT!'
                          '\n\nπ Π£Π·Π½Π°ΡΡ ΡΠ²ΠΎΠΉ ΡΡΠΎΠ²Π΅Π½Ρ Π·Π½Π°Π½ΠΈΠΉ π'
                          '\n\nπ ΠΡΠ΅Π³ΠΎ Π²ΠΎΠΏΡΠΎΡΠΎΠ²: 50'
                          '\nβ° ΠΠΈΠΌΠΈΡ Π²ΡΠ΅ΠΌΠ΅Π½ΠΈ: βΎ'
                          '\nβ ΠΡΠ°Π²ΠΈΠ»ΡΠ½ΡΠΉ ΠΎΡΠ²Π΅Ρ - 1 Π±Π°Π»Π»'
                          '\nβ ΠΠ΅Π²Π΅ΡΠ½ΡΠΉ ΠΎΡΠ²Π΅Ρ - 0 Π±Π°Π»Π»ΠΎΠ²'
                          '\n\nπ₯π₯π₯ ΠΠ΅ ΠΆΠ΄ΠΈΡΠ΅, Π½Π°ΡΠ½ΠΈΡΠ΅ ΡΠ΅ΠΉΡΠ°Ρ! ππ ΠΠ°ΠΆΠΌΠΈΡΠ΅ ΠΊΠ½ΠΎΠΏΠΊΡ'
                          ' "ππΊlevel testπ»π" Π½ΠΈΠΆΠ΅ ΠΈ ΠΏΡΠΎΠ²Π΅ΡΡΡΠ΅ ΡΠ²ΠΎΠΈ Π·Π½Π°Π½ΠΈΡ!'
                          '\n\nπ―ResultUZ: "From NO to YES"', reply_markup=TESTRU)

def mainCOURSERU(message):
    send_to_user(message.chat.id, 'ΠΡΡΡΡ ΡΡΠ΅Π±Π½ΠΎΠ³ΠΎ ΡΠ΅Π½ΡΡΠ° Result:\n'
                                  '\n β English Fundamentals'
                                  '\n β IELTS Master'
                                  '\n β IELTS 7+'
                                  '\n β IELTS FOCUS'
                                  '\n β Math in English'
                                  '\n ΠΠΈΠ½ΠΊ Π΄Π»Ρ ΠΏΠΎΠ΄ΡΠΎΠ±Π½ΠΎΠΉ ΠΈΠ½ΡΠΎΡΠΌΠ°ΡΠΈΠΈ ΠΎ ΠΊΡΡΡΠ°Ρ π'
                                  '\n https://www.result.uz/index.html#two', keyboardCourseRU)


def mainBranchesRU(message):
    send_to_user(message.chat.id, 'ΠΠ½ΠΈΠ·Ρ ΠΏΠΎΠ΄ΡΠΎΠ±Π½ΠΎΠ΅ ΠΈΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ ΠΎ Π½Π°ΡΠΈΡ  ΡΠΈΠ»ΠΈΠ°Π»Π°Ρ , ΠΡΠ±Π΅ΡΠΈΡΠ΅ Π½ΡΠΆΠ½ΡΠΉ Π²Π°ΠΌ ΡΠΈΠ»ΠΈΠ°Π».',
                 branchRU
                 )

def mentorsRU(message):
    send_to_user(message.chat.id, 'π Π‘ΠΏΠΈΡΠΎΠΊ ΠΊΠ²Π°Π»ΠΈΡΠΈΡΠΈΡΠΎΠ²Π°Π½Π½ΡΡ ΡΠΏΠ΅ΡΠΈΠ°Π»ΠΈΡΡΠΎΠ² ΡΡΠ΅Π±Π½ΠΎΠ³ΠΎ Π·Π°Π²Π΅Π΄Π΅Π½ΠΈΡ Result:'
                                  '\n\n1οΈβ£ - Harry Tompson \nIELTS Instructor\n'
                                  '\n2οΈβ£ - Mustafo Zafarovich \nIELTS Instructor\n'
                                  '\n3οΈβ£ - Rustam Umarovich \nLanguage Instructor\n'
                                  '\n4οΈβ£ - Abdurakhim Jalilov \nTESOL Certified Teacher\n'
                                  '\n5οΈβ£ - Sharof Rashidov \nIELTS Instructor\n'
                                  '\n6οΈβ£ - Aziz Normurodov \nLanguage Instructor\n'
                                  '\n7οΈβ£ - Bakhodir Abdullayev \nLanguage Instructor\n'
                                  '\n8οΈβ£ - Iskandarbek Kamoliddinov \nIELTS Instructor\n'
                                  '\n9οΈβ£ - Nasibaxon Raupova \nLanguage Instructor\n'
                                  '\nπ£π€ ΠΡΠ±Π΅ΡΠΈΡΠ΅ Π½Π°ΡΡΠ°Π²Π½ΠΈΠΊΠΎΠ², ΠΊΠΎΡΠΎΡΡΠ΅ Π²Π°ΠΌ ΠΈΠ½ΡΠ΅ΡΠ΅ΡΠ½Ρ'
                                  ' Π ΡΠ·Π½Π°ΠΉΡΠ΅ ΠΎ Π½ΠΈΡ Π±ΠΎΠ»ΡΡΠ΅!!', keyboard_techersRU)

def contactRU(message):
    send_to_photo(message.chat.id, open('Contact/contact-us.jpg', 'rb'),
                  'π ΠΠΎΠ½ΡΠ°ΠΊΡΡ| Telegram | Instagram'
                  '\n\n π RESULT SHCHOOL Π§ΠΈΠ»Π°Π½Π·Π°ΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                  '\n β Tel: +998 71 276 56 66'
                  '\n\n π RESULT SHCHOOL Π―ΠΊΠΊΠ°ΡΠ°ΡΠ°ΠΉΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                  '\n β Tel: +998 71 225 64 00'
                  '\n\n π RESULT SHCHOOL Π?Π½ΡΡΠ°Π±Π°Π΄ΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                  '\n β Tel: +998 71 120 22 21'
                  '\n\n π RESULT SHCHOOL Π¨Π°ΠΉΡΠ°Π½ΡΠ°ΡΡΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»'
                  '\n β Tel: +998 71 276 56 66'
                  '\n\nπLink: https://t.me/resultschool\n', InlineURLMessengersRU)


def settingsRU(message):
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.id, text='ΠΠ·ΠΌΠ΅Π½ΠΈΡΠ΅ ΡΠ·ΡΠΊ ΠΎΠ±ΡΠ΅Π½ΠΈΡ:',
                     reply_markup=inlineButtonLAN2)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    userId = message.chat.id
    text1 = 'πΊπΏ Assalomu alaykum! \nResultUZ Telegram botga xush kelibsiz! \nMuloqot tilini tanlang:' \
            '\n\nπ·πΊ ΠΠ΄ΡΠ°Π²ΡΡΠ²ΡΠΉΡΠ΅ ! \nΠΠΎΠ±ΡΠΎ ΠΏΠΎΠΆΠ°Π»ΠΎΠ²Π°ΡΡ Π² ΡΠ΅Π»Π΅Π³ΡΠ°ΠΌ Π±ΠΎΡ Result \nΠΠΎΠΆΠ°Π»ΡΠΉΡΡΠ° Π²ΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠ·ΡΠΊ Π΄Π»Ρ ΠΎΠ±ΡΠ΅Π½ΠΈΡ  '
    text2 = 'βοΈResultUZ botdan foydalanish yo`riqnomasi:' \
            '\nπΊπΏ O`zbek - o`zbek tili' \
            '\n\nBot komandalari:' \
            '\n /start komandasi - botni ishga tushirish' \
            '\n /help komandasi - botni ishlatish yo`riqnomasi' \
            '\n\nBot menyu:' \
            '\n π Level Test - Darajali test savollar' \
            '\n π Kurslar - ResultUZ kurslari' \
            '\n π Mentorlar - ResultUZ o`qituvchilar' \
            '\n π Filiallar - ResultUZ filiallari' \
            '\n π Kontaktlar - ResultUZ bilan aloqa' \
            '\n β Sozlamalar - Tilni o`zgartirish'\
            '\n\nβοΈΠΠ½ΡΡΡΡΠΊΡΠΈΡ ΠΏΠΎ ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°Π½ΠΈΡ Π±ΠΎΡΠ° ResultUZ:' \
            '\nπ·πΊ Π ΡΡΡΠΊΠΈΠΉ - Π ΡΡΡΠΊΠΈΠΉ ΡΠ·ΡΠΊ' \
            '\n\nΠΠΎΠΌΠ°Π½Π΄Ρ Π±ΠΎΡΠ°:' \
            '\n /start command - Π·Π°ΠΏΡΡΡΠΈΡΡ Π±ΠΎΡΠ°' \
            '\n /help command - ΠΈΠ½ΡΡΡΡΠΊΡΠΈΡ ΠΏΠΎ ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°Π½ΠΈΡ Π±ΠΎΡΠ°' \
            '\n\nΠΠ΅Π½Ρ Π±ΠΎΡΠ°:' \
            '\n π Π£Π·Π½Π°ΡΡ ΡΠ²ΠΎΠΉ ΡΡΠΎΠ²Π΅Π½Ρ Π·Π½Π°Π½ΠΈΠΉ π - ΠΠΎΠΏΡΠΎΡΡ Π΄Π»Ρ ΠΏΡΠΎΠ²Π΅ΡΠΊΠΈ ΡΡΠΎΠ²Π½Ρ' \
            '\n π ΠΠ°ΡΠΈ ΠΊΡΡΡΡ - ResultUZ ΠΊΡΡΡΡ' \
            '\n π ΠΠ°ΡΠΈ ΠΠ΅Π½ΡΠΎΡΡ - ResultUZ ΡΡΠΈΡΠ΅Π»Ρ' \
            '\n π ΠΠ°ΡΠΈ ΡΠΈΠ»ΠΈΠ°Π»Ρ - ResultUZ ΡΠΈΠ»ΠΈΠ°Π»Ρ' \
            '\n π ΠΠ°ΡΠΈ ΠΊΠΎΠ½ΡΠ°ΠΊΡΡr - Π‘Π²ΡΠ·Π°ΡΡΡΡ Ρ ResultUZ' \
            '\n β ΠΠ°ΡΡΡΠΎΠΉΠΊΠΈ - ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ ΡΠ·ΡΠΊ'
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
        send_to_user(userID, '<< ΠΠ»Π°Π²Π½ΠΎΠ΅ ΠΌΠ΅Π½Ρ >>', menyuRU)

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

    if message.text == 'π Level Test':
        levelTest(message)

    elif message.text == 'π Kurslar':
        mainCOURSE(message)

    elif message.text == 'π Mentorlar':
        mentors(message)

    elif message.text == 'π Filiallar':
        mainBranches(message)

    elif message.text == 'π Kontaktlar':
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

    elif message.text == 'π Orqaga':
        send_to_user(userId, '<< BOSH MENYU >>', menyu)

    elif message.text == 'β Sozlamalar':
        settings(message)

#====================================================== RUS ======================================================

    elif message.text == 'π Π£Π·Π½Π°ΡΡ ΡΠ²ΠΎΠΉ ΡΡΠΎΠ²Π΅Π½Ρ Π·Π½Π°Π½ΠΈΠΉ π':
        levelTestRU(message)

    elif message.text == 'π ΠΠ°ΡΠΈ ΠΊΡΡΡΡ':
        mainCOURSERU(message)

    elif message.text == 'π ΠΠ°ΡΠΈ ΠΠ΅Π½ΡΠΎΡΡ':
        mentorsRU(message)

    elif message.text == 'π ΠΠ°ΡΠΈ ΡΠΈΠ»ΠΈΠ°Π»Ρ':
        mainBranchesRU(message)

    elif message.text == 'π ΠΠ°ΡΠΈ ΠΊΠΎΠ½ΡΠ°ΠΊΡΡ':
        contactRU(message)

    elif message.text == 'Π§ΠΈΠ»Π°Π½Π·Π°ΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»':
        send_to_location(message.chat.id, 41.27673611459322, 69.20542894707292, message.id, branches1RU)
        # send_to_photo(userId, open('branchs/brchilanzar.jpg', 'rb'), )

    elif message.text == 'Π―ΠΊΠΊΠ°ΡΠ°ΡΠ°ΠΉΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»':
        send_to_location(message.chat.id, 41.28485458278078, 69.25611732008919, message.id, branches2RU)
        # send_to_photo(userId, open('branchs/bryakkasaroy.jpg', 'rb'),)

    elif message.text == 'Π?Π½ΡΡΠ°Π±Π°Π΄ΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»':
        # send_to_photo(userId, open('branchs/brmustaqillik.jpg','rb'),...)
        send_to_location(message.chat.id, 41.37455400878237, 69.29578031083248, message.id, branches3RU)

    elif message.text == 'Π¨Π°ΠΉΡΠ°Π½ΡΠ°ΡΡΡΡΠΊΠΈΠΉ ΡΠΈΠ»ΠΈΠ°Π»':
        send_to_location(message.chat.id, 41.32177771439208, 69.25375028331848, message.id, branches4RU)
        # send_to_photo(userId, open('branchs/brshayhontohur.jpg', 'rb'),)

    elif message.text == 'π ΠΠ°Π·Π°Π΄':
        send_to_user(message.chat.id, '<< ΠΠ»Π°Π²Π½ΠΎΠ΅ ΠΌΠ΅Π½Ρ >>', menyuRU)

    elif message.text == 'β ΠΠ°ΡΡΡΠΎΠΉΠΊΠΈ':
        settingsRU(message)

    else:
        bot.reply_to(message, message.text)  # reply rejimida javob qaytaradi

print('The telegram bot is working :)')

bot.polling(none_stop=True)
