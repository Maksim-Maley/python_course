import telebot 
import wikipedia 
import re 


bot = telebot.TeleBot('6078032789:AAEf8Z6ghbJrrKIlKtwIa-bSj8u8-O-VKBk')

wikipedia.set_lang('ru')

def getwiki(s):
    try:
        m = wikipedia.page(s)
        wikitext = m.content[:1000]
        wikidot = wikitext.split('.')
        wikiall = wikidot[:-1]
        wikitext2 = ''

        for i in wikidot:
            if not('==' in i):
                if(len((i.strip()))>3):
                    wikitext2 = wikitext2+i+'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return "я хз"

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id,"что надо говори")

@bot.message_handler(content_types=["text"])
def hand_t(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(non_stop=True, interval=0)
        