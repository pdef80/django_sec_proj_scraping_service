import transliterate
from langdetect import detect


def from_cyrillic_to_eng(text: str):
    ttx = text.replace(' ', '_').lower()
    if detect(ttx) == 'ru':
        return transliterate.translit(ttx, reversed=True)
    else:
        return ttx
