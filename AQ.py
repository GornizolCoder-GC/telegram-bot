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
                               '\n\n๐ก ResultUZ school - " from NO to YES ".'
                               '\n Learning is easy and exciting !!!'
                               '\n\n๐ O`zbekistondagi birinchi "Cambridge English Assessment" markazi'
                                '\n๐ "IELTS IDP" rasmiy hamkori'
                                '\nโ Call Center 78 113 32 32'
                               '\n\n๐Link: https://t.me/resultschool\n',
                       reply_markup=InlineURLMessengers)
        send_to_user(call.message.chat.id, 'Bu yerda siz o`zingiz uchun qiziqarli bo`lgan ma`lumotlarni olishingiz mumkin.'
                                           ' Kerakli menyuni tanlang: ', menyu)

#-------------------------------------------------- RUS --------------------------------------------------

    if call.data == 'ru':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, 'ะัะฑะตัะธัะต ะบะฐัะตะณะพัะธั ะฟะพะปัะทะพะฒะฐัะตะปั:', inlineButtonQARU)
    if call.data == 'stu':
        bot.delete_message(call.message.chat.id,
                           call.message.id)  # foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        send_to_user(call.message.chat.id, 'ะะฐะผ ะธะฝัะตัะตัะฝั ะธะฝะพัััะฐะฝะฝัะต ัะทัะบะธ ??', inlineButtonQA1RU)
    if call.data == 'parent':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, 'ะั ัะพัะธัะต ััะพะฑั ะฒะฐั ัะตะฑัะฝะพะบ ััะธะปัั ะฟัะฐะฒะธะปัะฝะพ ะธ ั ะปัััะธั ??',
                     inlineButtonQA1RU)

        # >>>>>>>>>>>>>>>>Rus SAVOLLAR UCHUN JOY SHU YERDA <<<<<<<<<<<<<<<<
    #continue...
    if call.data == 'da' or call.data == 'net':
        bot.delete_message(call.message.chat.id,
                           call.message.id)  # foydalanuvchidan kelgan xabarni uchirib keyin javob beradi
        bot.send_video(call.message.chat.id, open("video/ResultUzSchool.mp4", 'rb'),
                       caption='#ResulUz #resultschool #resultschoolbot'
                               '\n\n๐ก ResultUZ school - " from NO to YES ".'
                               '\n Learning is easy and exciting !!!'
                               '\n\n๐ ะะตัะฒัะน Cambridge English Assessment Center ะฒ ะฃะทะฑะตะบะธััะฐะฝะต'
                               '\n๐ "IELTS IDP" ะพัะธัะธะฐะปัะฝัะน ะฟะฐััะฝะตั'
                               '\nโ Call Center 78 113 32 32'
                               '\n\n๐Link: https://t.me/resultschool\n',
                       reply_markup=InlineURLMessengersRU)
        send_to_user(call.message.chat.id, 'ะะดะตัั ะฒั ะผะพะถะตัะต ะฟะพะปััะธัั ะธะฝัะตัะตัััััั ะฒะฐั ะธะฝัะพัะผะฐัะธั.'
                                           ' ะัะฑะตัะธัะต ะถะตะปะฐะตะผะพะต ะผะตะฝั: ', menyuRU)