from botToken import bot
from Inline_buttons import *
from buttons_inRussian import *
from sendFunctions import send_to_user


def call_courses(call):
    if call.data == 'course1':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ English Fundamentals'
                                           '\n\n📢 ResultUZ school to`g`ridan-to`g`ri ingliz tilining boshlang`ich darajasidagi kurslarni '
                                           'taklif qiladi, bu esa intensiv o`quv dasturini shakllantirishga mo`ljallangan bo`lib,'
                                           ' u boshlang`ich darajadagi asoslarni ham o`z ichiga oladi. '
                                           '\n⚡ Qisqa vaqt ichida '
                                           'ko`pchiligimiz til ko`nikmalarimizni yaxshilashimiz kerakligini tushunamiz va '
                                           'shu bilan biz o`quv jarayonining sifati va tezligini ta`kidlaymiz.'
                                           '\n🔥 Bu daraja'
                                           ' imtihonlardan muvaffaqiyatli o\'tish sharti bilan 2,5 oy davom etadi'
                                           '\n🔸 Pre Intermediate level lasts 2,5 oy.'
                                           '\n🔸 Intermediate level lasts 2,5 oy'
                                           '\n🔸 Upper Intermediate level lasts 2,5 oy'
                                           '\n🔸 Advanced level lasts 2,5 oy'
                                           '\n📌 Biz imtihonlarning murakkab tartibining muhimligiga ishonamiz, shuning uchun '
                                           'biz keyingi bosqichga o`tish paytida o`tkaziladigan imtihonlarning topshirilishi'
                                           ' va natijasini diqqat bilan kuzatib boramiz.', ManageButtonCourse)
    if call.data == 'course2':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS Master'
                                           '\n\n📌 Bizning IELTS Master -dagi keng qamrovli o`quv dasturimiz o`quvchilarga katta miqdordagi '
                                           'o`quv resurslarini taqdim etadi va bu materiallar maktabimiz mutaxassislari tomonidan sinchkovlik bilan tanlangan. '
                                           '\n🎯 Muvaffaqiyatli natijalarga erishish uchun biz o`quvchilarni barcha o`quv jarayoniga yo`naltiradigan muntazam '
                                           'imtihonlarni o`tkazamiz. '
                                           '\n🎯 Bu kurs ham hal qiluvchi ahamiyatga ega, chunki '
                                           'u e`tiborni IELTSga qaratadi va imtihonning barcha'
                                           ' bo`limlariga qaratilgan.', ManageButtonCourse)
    if call.data == 'course3':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS 7+'
                                           '\n\n🔥 Maktabimiz o`quvchilari 7+ dan ko`pchilikni tashkil etishi bilan faxrlanamiz,'
                                           ' ya`ni ingliz tilining yuqori darajadagi murakkabligidan qat`i nazar, '
                                           'o`quvchilarimiz hali ham o`z natijalariga g`ayratli va optimistik qarashadi. 😎😎😎'
                                           '\n🔹 Bu kurs butun jarayon davomida talabchan va amaliy tushuncha bilan mashhur, '
                                           'ayniqsa o`quv resurslari qamrab olinganda.'
                                           '\n🔹 Bu kurs juda samarali, chunki u mamlakatimizning eng yaxshi o`qituvchilari '
                                           'tomonidan boshqariladi.', ManageButtonCourse)
    if call.data == 'course4':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS FOCUS'
                                           '\n\n📌 Maktabimizda qilayotgan har bir ishimizning markazida eksklyuzivlik yotadi! '
                                           '\n♨ Talabalar natijalarini maksimal darajada oshirish uchun biz faqat IELTSning ichki '
                                           'va tashqi tomonlarini ko`rib chiqadigan o`quv dasturini ishlab chiqdik. '
                                           '\n🗝 Bu talabalarga nutq, tinglash, o`qish va yozish kabi to`rtta sohaning vaqt '
                                           'va zaifliklari bilan bog`liq muammolarni'
                                           ' bartaraf etishga yordam beradi.', ManageButtonCourse)
    if call.data == 'course5':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ Math in English'
                                           '\n\n🎯 Biz tushunamizki, xalqaro universitetlarda matematika bo`yicha kirish imtihonlari '
                                           'ingliz tilida bo`lib, bu universitetlarga hujjat topshirmoqchi bo`lgan talabalar '
                                           'uchun javobgarlikni ikki barobar oshiradi.'
                                           '\n🧩 Og`irlikni minimallashtirish va natijani maksimal darajada oshirish uchun'
                                           ' biz o`quvchilarni imtihondagi eng yomon vaziyatlarga tayyor va quvnoq his'
                                           ' qilishlariga yordam beradigan qisqartirilgan'
                                           ' o`quv dasturini ishlab chiqdik.', ManageButtonCourse)

#======================================================== RUS ========================================================

    if call.data == 'kurs1':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ English Fundamentals'
                                           '\n\n📢 ResultUZ school  напрямую предлагает курсы начального уровня английского языка,'
                                           'которые предназначены для формирования интенсивной программы, которая также включает в себя основы начального уровня. '
                                           ' Мы понимаем, что в наши дни многим из нас необходимо улучшить свои языковые навыки за короткий промежуток времени,'
                                           ' и поэтому мы подчеркиваем качество и скорость учебного процесса. '
                                           'Этот уровень длится 2,5 месяца при условии успешной сдачи экзаменов. '
                                           '\n🔸 Pre Intermediate level lasts 2,5 Месяц.'
                                           '\n🔸 Intermediate level lasts 2,5 Месяц.'
                                           '\n🔸 Upper Intermediate level lasts 2,5 Месяц.'
                                           '\n🔸 Advanced level lasts 2,5 Месяц.'
                                           '\n📌 Мы верим в важность жестких экзаменационных процедур,'
                                           'поэтому внимательно следим за сдачей и результатами экзаменов,'
                                           'которые проводятся, переходя на следующий уровень.',
                     ManageButtonCourseRU)
    if call.data == 'kurs2':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS Master'
                                           '\n\n📌 Наша обширная программа в IELTS Master предоставляет студентам огромное количество учебных ресурсов, '
                                           'и эти материалы были тщательно отобраны экспертами нашей школы. '
                                           '\n🎯 Чтобы обеспечить успешные результаты, мы проводим регулярные экзамены,'
                                           'которые направляют студентов на протяжении всего учебного процесса. '
                                           '\n🎯 Этот курс также имеет решающее значение,'
                                           ' поскольку он сосредоточен на мельчайших деталях IELTS и сосредоточен на всех разделах экзамена.'
                                           , ManageButtonCourseRU)
    if call.data == 'kurs3':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS 7+'
                                           '\n\n🔥 Мы гордимся тем, что ученики нашей школы составляют большинство в группе 7+,'
                                           ' а это означает, что, несмотря на сложность более высоких уровней английского языка, '
                                           ' наши ученики по-прежнему полны энтузиазма и оптимизма в отношении своих результатов. 😎😎😎'
                                           '\n🔹 Этот курс популярен благодаря своим требовательным и практическим знаниям на протяжении всего процесса, '
                                           'особенно когда речь идет об учебных ресурсах. '
                                           '\n🔹 Этот курс очень эффективен, так как его проводят лучшие учителя нашей страны. '
                                           , ManageButtonCourseRU)
    if call.data == 'kurs4':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ IELTS FOCUS'
                                           '\n\n📌 Эксклюзивность лежит в основе всего, что мы делаем в нашей школе!  '
                                           '\n♨ Чтобы максимизировать результаты студентов, мы разработали целенаправленную программу,'
                                           ' в которой рассматриваются только тонкости IELTS. '
                                           '\n🗝 Это помогает студентам преодолевать проблемы, связанные со временем и слабостями в конкретном разделе этих четырех областей, '
                                           'таких как разговорная речь, аудирование, чтение и письмо.'
                                           , ManageButtonCourseRU)
    if call.data == 'kurs5':
        bot.delete_message(call.message.chat.id, call.message.id)
        send_to_user(call.message.chat.id, '✅ Math in English'
                                           '\n\n🎯 Мы понимаем, что международные университеты проводят вступительные экзамены по математике на английском языке,  '
                                           'что вдвое увеличивает ответственность тех студентов, которые хотят поступить в эти университеты. '
                                           '\n🧩 Чтобы свести к минимуму нагрузку и максимизировать результат, мы разработали сжатую программу,'
                                           '  которая помогает студентам чувствовать себя готовыми и бодрыми даже в самых худших сценариях экзамена.'
                                            , ManageButtonCourseRU)
