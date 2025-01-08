class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for p in punctuation:
                    content = content.replace(p," ")

                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                positions[file_name] = words.index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)
        return counts

# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')

    print(finder.get_all_words())  # Все слова
    print(finder.find('TEXT'))  # 3 слово по счёту
    print(finder.count('teXT'))  # 4 слова teXT в тексте всего
