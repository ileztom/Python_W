import pandas as pd
def main():
    #1
    words = ['мама', 'мыла', 'раму']
    word_lengths = [len(word) for word in words]
    series_1 = pd.Series(word_lengths, index=words)
    print("Задание 1:")
    print(series_1)
    print()
    #2
    words = ['домик', 'и', 'лес', 'зверушка', 'опушка', 'странный']
    even_words = [word for word in words if len(word) % 2 == 0]
    odd_words = [word for word in words if len(word) % 2 != 0]
    series_even = pd.Series([len(word) for word in even_words], index=even_words)
    series_odd = pd.Series([len(word) for word in odd_words], index=odd_words)
    print("Задание 2:")
    print("Четные слова:")
    print(series_even)
    print("\nНечетные слова:")
    print(series_odd)
main()