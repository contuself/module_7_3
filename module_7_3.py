class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding = 'utf - 8') as f:
                words = []
                for line in f:
                    line = line.lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(punct, '')
                    words.extend(line.split())
            all_words[i] = words
        return all_words

    def find(self, word):
        result = {}
        for i, words in self.get_all_words().items():
            word = word.lower()
            result[i] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        for i, words in self.get_all_words().items():
            word = word.lower()
            result[i] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего
