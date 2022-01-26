from botToken import bot

#########################################################################################################

def send_to_user(id, text, buttons):
    bot.send_message(id, text, reply_markup=buttons)

def send_to_photo(id, pict,text, buttons):
    bot.send_photo(id, photo=pict, caption=text, reply_markup=buttons)

def send_to_location(id,lati,longi, message_id, buttons):
    bot.send_location(id, latitude=lati, longitude=longi,reply_to_message_id=message_id, reply_markup=buttons )

def echo(id, text):
    bot.send_message(id, text)