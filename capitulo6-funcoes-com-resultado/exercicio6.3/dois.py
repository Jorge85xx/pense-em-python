"""Escreva uma função chamada is_palindrome que
receba uma string como argumento e retorne True se
for um palíndromo e False se não for. Lembre-se de
que você pode usar a função integrada len para
verificar o comprimento de uma string."""

def  is_palindrome(word):
  string_palindrome = ""
  for i in range(len(word)-1, -1, -1):
    string_palindrome += word[i]
  return string_palindrome == word

print(is_palindrome('oioo'))
words = ["ovo", "arara", "radar", "reger", "asa", "mirim", "reviver", "osso", "omissíssimo", "reconhecer"]

for word in words:
    print(f"A palavra '{word}' é um palíndromo? {is_palindrome(word)}")

"outra maneira de fazer"
def is_palindrome(s):
    return s == s[::-1]