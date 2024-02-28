def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

arrays = [
    ["Hello", "2", "world", ":-)"],
    ["1234", "1567", "-2", "computer science"],
    ["Russia", "Denmark", "Kazan"]
]

for strings in arrays:
    print(f"Оригинальный массив:        {strings}")
    filtered_strings = filter_strings(strings)
    print(f"Отфильтрованный массив:     {filtered_strings}")
