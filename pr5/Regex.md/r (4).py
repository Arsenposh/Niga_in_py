import re

text = input("Введите текст: ")
pattern = r'[A-ZА-Я][a-zа-я]+'
results = re.findall(pattern, text)

print("Найдено:", results if results else "Ничего не нашлось")
