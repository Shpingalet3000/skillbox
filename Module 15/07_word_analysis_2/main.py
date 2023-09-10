word = input("Введите слово: ")
word_backwards = []
word_palindrome = True
for i in range(len(word)):
    if word[i] != word[-i - 1]:
        word_palindrome = False
        break
if word_palindrome is True:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

print("\nВторой вариант")

if word == word[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
