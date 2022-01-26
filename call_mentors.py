from Inline_buttons import *
from buttons_inRussian import *
from botToken import bot


def call_mentors(call):
    if call.data == 't1':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/HarryTompson.jpg', 'rb'),
                       caption='1️⃣ - Mentor\n\n🤵‍♂️Teacher: Harry Tompson \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't2':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/MustafoZafarovich.jpg', 'rb'),
                       caption='2️⃣ - Mentor\n\n🤵‍♂️Teacher: Mustafo Zafarovich \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't3':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/RustamUmarovich.jpg', 'rb'),
                       caption='3️⃣ - Mentor\n\n🤵‍♂️Teacher: Rustam Umarovich \n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't4':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/AbdurakhimJalilov.jpg', 'rb'),
                       caption='4️⃣ - Mentor\n\n🤵‍♂️Teacher: Abdurakhim Jalilov \n🔺 TESOL Certified Teacher\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't5':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/Sharof Rashidov.jpg', 'rb'),
                       caption='5️⃣ - Mentor \n\n🤵‍♂️Teacher:  Sharof Rashidov \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't6':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/AzizNormurodov.jpg', 'rb'),
                       caption='6️⃣ - Mentor\n\n🤵‍♂️Teacher: Aziz Normurodov \n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't7':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/BakhodirAbdullayev.jpg', 'rb'),
                       caption='7️⃣ - Mentor\n\n🤵‍♂️Teacher: Bakhodir Abdullayev\n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't8':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/IskandarbekKamoliddinov.jpg', 'rb'),
                       caption='8️⃣ - Mentor\n\n🤵‍♂️Teacher: Iskandarbek Kamoliddinov \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentors)
    if call.data == 't9':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/NasibaxonRaupova.jpg', 'rb'),
                       caption='9️⃣ - Mentor\n\n🤵‍♀️️Teacher: Nasibaxon Raupova\n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentors)

#=============================================== RUS ===============================================

    if call.data == 'f1':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/HarryTompson.jpg', 'rb'),
                       caption='1️⃣ - Mentor\n\n🤵‍♂️Teacher: Harry Tompson \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f2':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/MustafoZafarovich.jpg', 'rb'),
                       caption='2️⃣ - Mentor\n\n🤵‍♂️Teacher: Mustafo Zafarovich \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f3':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/RustamUmarovich.jpg', 'rb'),
                       caption='3️⃣ - Mentor\n\n🤵‍♂️Teacher: Rustam Umarovich \n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f4':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/AbdurakhimJalilov.jpg', 'rb'),
                       caption='4️⃣ - Mentor\n\n🤵‍♂️Teacher: Abdurakhim Jalilov \n🔺 TESOL Certified Teacher\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f5':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/Sharof Rashidov.jpg', 'rb'),
                       caption='5️⃣ - Mentor \n\n🤵‍♂️Teacher:  Sharof Rashidov \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f6':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/AzizNormurodov.jpg', 'rb'),
                       caption='6️⃣ - Mentor\n\n🤵‍♂️Teacher: Aziz Normurodov \n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f7':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/BakhodirAbdullayev.jpg', 'rb'),
                       caption='7️⃣ - Mentor\n\n🤵‍♂️Teacher: Bakhodir Abdullayev\n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f8':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/IskandarbekKamoliddinov.jpg', 'rb'),
                       caption='8️⃣ - Mentor\n\n🤵‍♂️Teacher: Iskandarbek Kamoliddinov \n🔺 Specialization: IELTS Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
    if call.data == 'f9':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, open('teachers_photo/NasibaxonRaupova.jpg', 'rb'),
                       caption='9️⃣ - Mentor\n\n🤵‍♀️️Teacher: Nasibaxon Raupova\n🔺 Language Instructor\n',
                       reply_markup=ManageButtonMentorsRU)
