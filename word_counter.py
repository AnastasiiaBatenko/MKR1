import re
from collections import Counter

def read_file(filepath):
    """
    Зчитує вміст текстового файлу.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None

def preprocess_text(text):
    """
    Видаляє нелітерні символи та приводить текст до нижнього регістру.
    """
    if text is None:
        return ""
    text = re.sub(r'[^a-zA-Zа-яА-ЯіїєІЇЄ\s]', '', text)
    return text.lower()

def count_words(text):
    """
    Розбиває текст на слова та підраховує їхню кількість.
    """
    words = text.split()
    return Counter(words)
