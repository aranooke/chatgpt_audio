from translate import Translator
from langdetect import detect
def translate_text(text, source_lang, target_lang):
    
    lang_detect = detect(text);
    translator = Translator(from_lang=lang_detect, to_lang=target_lang)
    translation = translator.translate(text)
    return translation

print(translate_text("це рідна мова","en","en"))
# Пример использования

