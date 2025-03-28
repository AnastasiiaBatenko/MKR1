import pytest
from collections import Counter
from word_counter import read_file, preprocess_text, count_words, get_top_n_words, write_results_to_file
import os

# Фікстура для створення тимчасового файлу
@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "temp_text.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Це тестовий текст. Тестовий текст містить кілька слів. Кілька.")
    return str(file_path)

def test_read_file(temp_file):
    content = read_file(temp_file)
    assert content == "Це тестовий текст. Тестовий текст містить кілька слів. Кілька."
    assert read_file("non_existent_file.txt") is None
