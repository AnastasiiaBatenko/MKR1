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
