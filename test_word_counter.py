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

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Це тестовий текст.", "це тестовий текст"),
        ("123 Hello, World!", " hello world"),
        ("Привіт Світ!", "привіт світ"),
        (None, ""),
        ("", ""),
    ],
)
def test_preprocess_text(input_text, expected_output):
    assert preprocess_text(input_text) == expected_output

def test_count_words():
    text = "це тестовий текст тестовий"
    expected_counts = Counter({"це": 1, "тестовий": 2, "текст": 1})
    assert count_words(text) == expected_counts

def test_get_top_n_words():
    word_counts = Counter({"a": 5, "b": 3, "c": 1, "d": 4})
    assert get_top_n_words(word_counts, 2) == [("a", 5), ("d", 4)]
    assert get_top_n_words(word_counts, 5) == [("a", 5), ("d", 4), ("b", 3), ("c", 1)]
    assert get_top_n_words(word_counts, 0) == []

def test_write_results_to_file(tmp_path):
    output_file = tmp_path / "output.txt"
    top_words = [("слово", 5), ("ще", 3)]
    write_results_to_file(str(output_file), top_words)
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "слово-5\nще-3\n"

def test_main_integration(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "top_words.txt"
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("apple banana apple orange banana apple")
    from word_counter import main
    main(str(input_file), str(output_file))
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read().strip().split('\n')
    assert "apple-3" in content
    assert "banana-2" in content
    assert len(content) <= 10
