import iso639
from langdetect import detect
def recognize_language_from_text(text):
    language_code = detect(text)
    language = get_language_name_by_code(language_code)
    return language

def get_language_name_by_code(language_code):
    try:
        language = iso639.languages.get(alpha2=language_code)
        return language.name
    except KeyError:
        return "Unknown Language"