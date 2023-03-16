import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
token='5604059957:AAH6qr3UjsxQRTA5mooQMaBmGd2BwUGL_I8'
bot=telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def any_msg(message):    
    start_keyboard = InlineKeyboardMarkup()
    callback_button = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
    start_keyboard.add(callback_button)
    user_first_name = str(message.chat.first_name)
    bot.reply_to(message, f"Привет {user_first_name} ✌️ ты попал в RussianShop, переходи к покупкам!", reply_markup=start_keyboard)

def show_item(call, path_to_picture, cb_data, name):
    name = cb_data.split('|')[1]
    buy_keyboard = InlineKeyboardMarkup(row_width=1)
    callback_button = InlineKeyboardButton(text="Купить", callback_data=cb_data)
    callback_button2 = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
    buy_keyboard.add(callback_button, callback_button2)
    photo = open(path_to_picture, 'rb')
    msg = bot.send_photo(chat_id=call.message.chat.id, 
                         photo=photo, 
                         caption=f'{name}', 
                         reply_markup=buy_keyboard)
    
# def show_button(call):
#     buy_keyboard2 = InlineKeyboardMarkup(row_width=1)
#     callback_button = InlineKeyboardButton(text="Купить", callback_data="Купить")
#     callback_button2 = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
#     buy_keyboard2.add(callback_button, callback_button2)
#     msg = bot.send_message(chat_id=call.message.chat.id,  
#                            text='Прекрасный выбор', 
#                            reply_markup=buy_keyboard2)    



def providing_name_callback(msg, name):
    print(msg)
    str = f'username={msg.from_user.username}, text={msg.text}, item_name={name}'
    chat_id= 5495705118
    bot.send_message(chat_id=chat_id, text=str)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Каталог":  
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)          
            button_keyboard = InlineKeyboardMarkup(row_width=1)
            callback_button = InlineKeyboardButton(text="Табак", callback_data="Табак")
            callback_button2 = InlineKeyboardButton(text="Сигареты", callback_data="Сигареты")                          
            callback_button3 = InlineKeyboardButton(text="Glo", callback_data="Glo")
            button_keyboard.add(callback_button,
                         callback_button2,
                         callback_button3)
            msg=bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбери категорию',
                reply_markup=button_keyboard)

        
        
                
        if call.data == 'Табак':                      
            button_tabak = InlineKeyboardMarkup(row_width=1)
            callback_button = InlineKeyboardButton(text="Bali Shag Halfzware, 8500 LKR", callback_data="Bali Shag Halfzware")
            callback_button2 = InlineKeyboardButton(text="Dark Chocolate, 8500 LKR", callback_data="Dark Chocolate")
            callback_button3 = InlineKeyboardButton(text="Bali Nature, 8500 LKR", callback_data="Bali Nature")
            callback_button4 = InlineKeyboardButton(text="Vanilla Choice, 8500 LKR", callback_data="Vanilla Choice")
            callback_button5 = InlineKeyboardButton(text="Aromatic Choice, 8500 LKR", callback_data="Aromatic Choice")
            callback_button6 = InlineKeyboardButton(text="Virginia Blend, 8500 LKR", callback_data="Virginia Blend")
            callback_button7 = InlineKeyboardButton(text="Cherry, 8500 LKR", callback_data="Cherry")
            callback_button8 = InlineKeyboardButton(text="Pandan, 8500 LKR", callback_data="Pandan")
            callback_button9 = InlineKeyboardButton(text="Exotic, 8500 LKR", callback_data="Exotic")
            callback_button10 = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
            button_tabak.add(callback_button,
                                callback_button2,
                                callback_button3,
                                callback_button4,
                                callback_button5,
                                callback_button6,
                                callback_button7,
                                callback_button8,
                                callback_button9,
                                callback_button10)

        # try:                      
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Табак",
                reply_markup=button_tabak)                   
        # except Exception as e:
        #  print('Error:', e)


        if call.data == 'Bali Shag Halfzware':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Bali Shag.jpg', "ITEM|Bali Shag", 'Bali Shag Halfzware')
        
        if call.data == 'Dark Chocolate':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Dark Chocolate.jpg', "ITEM|Dark Chocolate", 'Dark Chocolate')

        if call.data == 'Bali Nature':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)   
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Bali Nature.jpg', "ITEM|Bali Nature", 'Bali Nature')

        if call.data == 'Vanilla Choice':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Vanilla Choice.jpg', "ITEM|Vanilla Choice", 'Vanilla Choice') 

        if call.data == 'Aromatic Choice':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Aromatic Choice.jpg', "ITEM|Aromatic Choice", 'Aromatic Choice')
            
        if call.data == 'Virginia Blend':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Virginia Blend.jpg', "ITEM|Virginia Blend", 'Virginia Blend')
            
        if call.data == 'Cherry':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Cherry.jpg', "ITEM|Cherry", 'Cherry')
            
        if call.data == 'Pandan':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Pandan.jpg', "ITEM|Pandan", 'Pandan')
            
        if call.data == 'Exotic':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Exotic.jpg', "ITEM|Exotic", 'Exotic')

        if call.data == 'Сигареты':
            button_sigarets = InlineKeyboardMarkup(row_width=1)
            callback_button = InlineKeyboardButton(text="Captain Black\nGrape, 3000 LKR", callback_data="Captain Black\nGrape")
            callback_button2 = InlineKeyboardButton(text="Chapman, 3000 LKR", callback_data="Chapman")
            callback_button3 = InlineKeyboardButton(text="Parlament Silver, 3000 LKR", callback_data="Parlament Silver")
            callback_button4 = InlineKeyboardButton(text="Kent Switch, 3000 LKR", callback_data="Kent Switch")
            callback_button5 = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
            button_sigarets.add(callback_button,
                                callback_button2,
                                callback_button3,
                                callback_button4,
                                callback_button5)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Сигареты",
                reply_markup=button_sigarets)


        if call.data == 'Captain Black\nGrape':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)   
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Captain Black Grape.jpg', "ITEM|Captain Black\nGrape", 'Captain Black\nGrape')
            
        if call.data == 'Chapman':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Chapman.jpg', "ITEM|Chapman", 'Chapman')

            
        if call.data == 'Parlament Silver':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Parlament Silver.jpg', "ITEM|Parlament Silver", 'Parlament Silver')
            
        if call.data == 'Kent Switch':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Kent Switch.png', "ITEM|Kent Switch", 'Kent Switch')

                         
       
        if call.data == 'Glo':   
            button_glo = InlineKeyboardMarkup(row_width=1)
            callback_button_glo = InlineKeyboardButton(text='Glo Black, 10000 LKR', callback_data='Glo Black')
            callback_button_glo2 = InlineKeyboardButton(text='Glo Blue, 10000 LKR', callback_data='Glo Blue') 
            button_glo.add(callback_button_glo,
                           callback_button_glo2)    
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Glo",
                reply_markup=button_glo)
            
        if call.data == 'Glo Black':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Glo Black.png', "ITEM|Glo Black", 'Glo Black')
            
        if call.data == 'Glo Blue':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)    
            show_item(call,'/Users/mr.robot/Documents/russhop/img/Glo Blue.jpg', "ITEM|Glo Blue", 'Glo Blue')

        
        

        if call.data.split('|')[0] == 'ITEM':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            msg=bot.send_message(
                chat_id=call.message.chat.id,
                text="Оставьте контактные данные, с вами свяжутся",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg, providing_name_callback, call.data.split('|')[1])
        
      

if __name__ == '__main__':
 bot.infinity_polling(timeout=10, long_polling_timeout = 5)




