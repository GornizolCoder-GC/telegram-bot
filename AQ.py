from sendFunctions import  *
from Inline_buttons import *
from buttons_inRussian import *
from Reply_buttons import *
from botToken import bot

def aq(call):
    if call.data == 'uz':
        bot.delete_message(call.message.chat.id, call.message.id) #foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        send_to_user(call.message.chat.id, 'Foydalanuvchi turini tanlang:', inlineButtonQA)

    if call.data == 'T' or call.data == 'family' :
        bot.delete_message(call.message.chat.id, call.message.id) #foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        send_to_user(call.message.chat.id, 'Oxirgi 1 oy davomida YouTube orqali til o\'rganishga oid '
                                           'darslik tomosha qildingizmi? ', inlineButtonQA1)

        # >>>>>>>>>>>>>>>>Uzb SAVOLLAR UCHUN JOY SHU YERDA <<<<<<<<<<<<<<<<
    # continue...
    if call.data == 'yes' or call.data == 'no' :
        bot.delete_message(call.message.chat.id, call.message.id) #foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        bot.send_video(call.message.chat.id, open("video/ResultUzSchool.mp4", 'rb'),
                       caption='#ResulUz #resultschool #resultschoolbot'
                               '\n\n💡 ResultUZ school - " from NO to YES ".'
                               '\n Learning is easy and exciting !!!'
                               '\n\n📚 O`zbekistondagi birinchi "Cambridge English Assessment" markazi'
                                '\n📝 "IELTS IDP" rasmiy hamkori'
                                '\n☎ Call Center 78 113 32 32'
                               '\n\n👉Link: https://t.me/resultschool\n',
                       reply_markup=InlineURLMessengers)
        send_to_user(call.message.chat.id, 'Bu yerda siz o`zingiz uchun qiziqarli bo`lgan ma`lumotlarni olishingiz mumkin.'
                                           ' Kerakli menyuni tanlang: ', menyu)

#-------------------------------------------------- RUS --------------------------------------------------

    if call.data == 'ru':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, 'Выберите категорию пользователя:', inlineButtonQARU)
    if call.data == 'stu':
        bot.delete_message(call.message.chat.id,
                           call.message.id)  # foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        send_to_user(call.message.chat.id, 'Вам интересны иностранные языки ??', inlineButtonQA1RU)
    if call.data == 'parent':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, 'Вы хотите чтобы ваш ребёнок учился правильно и у лучших ??',
                     inlineButtonQA1RU)

        # >>>>>>>>>>>>>>>>Rus SAVOLLAR UCHUN JOY SHU YERDA <<<<<<<<<<<<<<<<
    #continue...
    if call.data == 'da' or call.data == 'net':
        bot.delete_message(call.message.chat.id,
                           call.message.id)  # foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        bot.send_video(call.message.chat.id, open("video/ResultUzSchool.mp4", 'rb'),
                       caption='#ResulUz #resultschool #resultschoolbot'
                               '\n\n💡 ResultUZ school - " from NO to YES ".'
                               '\n Learning is easy and exciting !!!'
                               '\n\n📚 Первый Cambridge English Assessment Center в Узбекистане'
                               '\n📝 "IELTS IDP" официальный партнер'
                               '\n☎ Call Center 78 113 32 32'
                               '\n\n👉Link: https://t.me/resultschool\n',
                       reply_markup=InlineURLMessengersRU)
        send_to_user(call.message.chat.id, 'Здесь вы можете получить интересующую вас информацию.'
                                           ' Выберите желаемое меню: ', menyuRU)