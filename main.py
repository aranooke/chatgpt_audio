import telebot,os,convert
from convert import convert_ogg_to_wav;
import speech
import to_speech;
from telebot import types
from chatgpt import ask_gpt
from trans import translate_text
bot = telebot.TeleBot("6054271853:AAGn-jrBu1FzN1HTR3yzY7YknT7DrSHwnYg", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
language = "en-US";
buttons = ['English','Українська','Російська'];
langs = ["en-US","uk-UA","ru-RU"]
txt = "";
@bot.message_handler(commands=['send'])
def send_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text="Перевести на русский", callback_data="translate_ru")
    url2 = types.InlineKeyboardButton(text="Перевести на украинский",  callback_data="translate_ua")
    keyboard.add(url1,url2);
    text =  message.text.split('/send ')[1]
    bot.send_message(message.chat.id,f"You said:{text}");
    bot.send_message(message.chat.id,ask_gpt(text),reply_markup=keyboard);
def call_translate(message):
    res = message;
    if len(res) < 500:
        res = translate_text(call.message.text,"en","ru");
        bot.send_message(call.message.chat.id,res);
    else:
        res = res[0:500-1];
        bot.send_message(call.message.chat.id,res);
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "translate_ru":
        # Handle translation to Russian
        bot.send_message(call.message.chat.id, "Translating to Russian...")
        res = call.message.text;
        if len(res) < 500:
            res = translate_text(call.message.text,"en","ru");
            bot.send_message(call.message.chat.id,res);
        else:
            res = translate_text(res[0:500-1],"en","ru");
            bot.send_message(call.message.chat.id,res);
        # Your translation logic here
    elif call.data == "translate_ua":
        # Handle translation to Ukrainian
        bot.send_message(call.message.chat.id, "Translating to Ukrainian...")
        res = call.message.text;
        if len(res) < 500:
            res = translate_text(call.message.text,"en","uk");
            bot.send_message(call.message.chat.id,res);
        else:
            res = translate_text(res[0:500-1],"en","uk");
            bot.send_message(call.message.chat.id,res);
    elif call.data == "make_loud":
        bot.send_message(call.message.chat.id, "Make loud...")
        to_speech.text_to_speech(call.message.text,"output.wav");
        with open("output.wav", 'rb') as voice:
            bot.send_voice(call.message.chat.id, voice);
        # Your translation logic here
    else:
        # Handle other callback data if needed
        pass    
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path);  
    with open("main.ogg","wb")as new_file:
        new_file.write(downloaded_file);
    convert_ogg_to_wav(); 
    text = speech.recognize_speech()
    bot.send_message(message.chat.id,f'You said:{text}');
    result_from_gpt = ask_gpt(text,temperature=0.5,max_tokens=512);
    bot.send_message(message.chat.id, result_from_gpt);    
@bot.message_handler(commands=["select"])
def select_lang(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    for key in buttons:
        keyboard.add(key)
    bot.send_message(message.chat.id, 'Select a language:', reply_markup=keyboard) 

    print(language);

@bot.message_handler(content_types=['text'])
def text_work(message):
    for key in range(len(buttons)):
        if buttons[key] == message.text:
            language = langs[key];
            bot.send_message(message.chat.id,f" {language}({buttons[key]}) обрана");
    if message.text == "Перевести на русский":
        bot.send_message(message.chat.id,translate_text(txt,"en","ru"));
    elif message.text == "Перевести на украинский":
        bot.send_message(message.chat.id,translate_text(txt,"en","ua"));

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    # Check if an audio file is attached to the message
    if message.audio:
        file_id = message.audio.file_id
        file_info = bot.get_file(file_id)

        # Download the file
        downloaded_file = bot.download_file(file_info.file_path)

        # Specify the directory to save the audio files
        save_directory = 'path/to/save/audiofiles/'

        # Create the save directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Generate a unique filename for the audio file
        file_extension = os.path.splitext(file_info.file_path)[-1]
        filename = f'{file_id}{file_extension}'

        # Save the downloaded file
        save_path = os.path.join(save_directory, filename)
        with open(save_path, 'wb') as file:
            file.write(downloaded_file)
        bot.reply_to(message, "Audio file saved successfully.")
        convert.convert(save_path);
        text = speech.recognize_speech("file.wav");
        bot.send_message(message.chat.id,f"You said:{text}");
        print(text);
        res = ask_gpt(text);
        
        with open("file.wav", 'rb') as voice:
            bot.send_voice(message.chat.id, voice);
        keyb = types.InlineKeyboardMarkup()
        text_loud = types.InlineKeyboardButton(text="Озвучить текст", callback_data="make_loud")
        keyb.add(text_loud);
        bot.send_message(message.chat.id,res,reply_markup=keyb);

        
        # Send a confirmation message to the user
    else:
        # Handle the case when no audio file is attached
        bot.reply_to(message, "No audio file attached.")

# Start the bot and listen for incoming updates
bot.polling()