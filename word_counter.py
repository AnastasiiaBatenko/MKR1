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

def get_top_n_words(word_counts, n=10):
    """
    Повертає список з n найпопулярніших слів та їх кількість.
    """
    return word_counts.most_common(n)

def write_results_to_file(filepath, top_words):
    """
    Записує результати у файл у форматі "слово-кількість".
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for word, count in top_words:
            f.write(f"{word}-{count}\n")

def main(input_filepath, output_filepath="top_words.txt"):
    """
    Основна функція для обробки файлу та запису результатів.
    """
    content = read_file(input_filepath)
    if content is None:
        print(f"Помилка: Файл '{input_filepath}' не знайдено.")
        return

    processed_text = preprocess_text(content)
    word_counts = count_words(processed_text)
    top_words = get_top_n_words(word_counts)
    write_results_to_file(output_filepath, top_words)
    print(f"Топ-10 слів записано у файл '{output_filepath}'.")

if __name__ == "__main__":
    input_file = input("Введіть шлях до вхідного .txt файлу: ")
    main(input_file)
