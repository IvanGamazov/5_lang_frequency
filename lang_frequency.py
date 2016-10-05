import re
import collections


def load_data(file_path):
    with open(file_path) as text_for_analysis:
        lower_case_text = text_for_analysis.read().lower()
        return lower_case_text


def get_most_frequent_words(text, count):
    words = re.findall(r'\w+', text)
    common_words = collections.Counter(words).most_common(count)
    return common_words


if __name__ == '__main__':
    filepath = input("Укажите файл для анализа --> ")
    words_count = 0
    while words_count < 1:
        words_count = int(input("Сколько самых популярных слов вывести на экран? --> "))
    text_to_analyse = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text_to_analyse, words_count)
    for word in most_frequent_words:
        print("Слово:", word[0], "Число вхождений:", word[1])


