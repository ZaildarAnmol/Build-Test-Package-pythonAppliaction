from googletrans import Translator

def englishToFrench(englishText):
    """
    Translate English text to French.
    """
    translator = Translator()
    frenchText = translator.translate(englishText, src='en', dest='fr').text
    return frenchText

def frenchToEnglish(frenchText):
    """
    Translate French text to English.
    """
    translator = Translator()
    englishText = translator.translate(frenchText, src='fr', dest='en').text
    return englishText
