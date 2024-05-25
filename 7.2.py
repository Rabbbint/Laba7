def find_max_substring_multiplicity(word, substring):

    max_multiplicity = 0
    current_multiplicity = 0
    index = 0

    while index <= len(word) - len(substring):
        if word[index:index + len(substring)] == substring:
            current_multiplicity += 1
            max_multiplicity = max(max_multiplicity, current_multiplicity)
            index += len(substring)
        else:
            current_multiplicity = 0
            index += 1

    return max_multiplicity


word = input("Введите поисковый запрос: ")
substring = input("Введите подстроку для анализа: ")

max_multiplicity = find_max_substring_multiplicity(word, substring)
print(f"Максимальная кратность подстроки '{substring}' в запросе '{word}': {max_multiplicity}")
