from collections import defaultdict
from translate import Translator 

# Görev #5: Soruları soru işareti ve boşluk olmadan yazıyoruz
qwestions = {
    "adın ne": "ben süper havalı bir botum ve amacım size yardım etmek!",
    "kaç yaşındasın": "bu çok felsefi bir soru...",
    "hangi dilleri konuşuyorsun": "ben sadece Türkçe ve İngilizce konuşabiliyorum"
}

class TextAnalysis():    
    # Görev #1
    memory = defaultdict(list)
    
    def __init__(self, text, owner):
        # Görev #2
        TextAnalysis.memory[owner].append(self)
        self.text = text # kullanıcının girdiği metin
        
        # Soru işaretini, noktayı ve büyük harfleri otomatik temizliyoruz
        clean_text = self.text.lower().strip(" ?.!")

        # Görev #6: Sözlük kontrolü
        if clean_text in qwestions.keys():
            self.response = qwestions[clean_text]
        else:
            self.response = self.get_answer()
            
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation 
        except:
            return "Çeviri girişimi başarısız oldu"