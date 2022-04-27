from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_ru = InlineKeyboardButton('Россия', callback_data="ru")
button_fr = InlineKeyboardButton('Франция', callback_data="fr")
button_bu = InlineKeyboardButton('Беларусь', callback_data="by")
button_sp = InlineKeyboardButton('Испания', callback_data="es")
button_kz = InlineKeyboardButton('Казахстан', callback_data="kz")
button_kz = InlineKeyboardButton('Нидерланды', callback_data="nl")

kb_choiсe_country = InlineKeyboardMarkup().add(button_bu,button_fr,button_kz,button_ru,button_sp)

def create_button(country_domen):
    global button_ya, button_you, button_google, button_inst, inline_keyboard_sites, inline_keyboard_sites
    if country_domen == "fr" or country_domen == "nl" or country_domen == "es":        
        button_ya = InlineKeyboardButton('Yandex', url="https://yandex.eu/")
        button_you = InlineKeyboardButton('YouTube', url="https://youtube." + country_domen + "/")
        button_google = InlineKeyboardButton('Google', url="https://google." + country_domen + "/")
        button_inst = InlineKeyboardButton('Instagram', url="https://instagram.com/")
        inline_keyboard_sites = InlineKeyboardMarkup().add(button_ya,button_google,button_inst,button_you)
        inline_keyboard_sites = InlineKeyboardMarkup().row(button_ya,button_google,button_inst,button_you)
    else:
        button_ya = InlineKeyboardButton('Yandex', url="https://yandex." + country_domen + "/")
        button_you = InlineKeyboardButton('YouTube', url="https://youtube." + country_domen + "/")
        button_google = InlineKeyboardButton('Google', url="https://google." + country_domen + "/")
        button_inst = InlineKeyboardButton('Instagram', url="https://instagram.com/")
        inline_keyboard_sites = InlineKeyboardMarkup().add(button_ya,button_google,button_inst,button_you)
        inline_keyboard_sites = InlineKeyboardMarkup().row(button_ya,button_google,button_inst,button_you)

