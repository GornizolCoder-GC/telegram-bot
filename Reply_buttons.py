import telebot

# 000000------> MENYU - REPLY_KEYBOARD_MARKUP <------000000
#UZBEK
menyu = telebot.types.ReplyKeyboardMarkup(True, True)
menyu.row('🏁 Level Test')
menyu.row('📝 Kurslar','🎓 Mentorlar')
menyu.row('📞 Kontaktlar','📍 Filiallar')
menyu.row('⚙ Sozlamalar')

#RUS
menyuRU = telebot.types.ReplyKeyboardMarkup(True, True)
menyuRU.row('🏁 Узнать свой уровень знаний 🏁')
menyuRU.row('📝 Наши курсы', '🎓 Наши Менторы')
menyuRU.row('📞 Наши контакты', '📍 Наши филиалы')
menyuRU.row('⚙ Настройки')

# 000000------> Filiallar - REPLY_KEYBOARD_MARKUP <------000000
#UZBEK
branch = telebot.types.ReplyKeyboardMarkup(True,True)
branch.row('Chilonzor filiali',
           'Yakkasaroy filiali')
branch.row('Mustaqillik filiali',
           'Shayxontohur filiali')
branch.row('🔙 Orqaga')

#RUS
branchRU = telebot.types.ReplyKeyboardMarkup(True, True)
branchRU.row('Чиланзарский филиал',
           'Яккасарайский филиал')
branchRU.row('Юнусабадский филиал',
           'Шайхантахурский филиал')
branchRU.row('🔙 Назад')
# ----------------------------------------------------
