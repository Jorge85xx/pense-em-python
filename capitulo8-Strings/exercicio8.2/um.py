"""Há um método de string chamado count, que é
semelhante à função em “Loop e contagem”, na página
123. Leia a documentação deste método e escreva uma
invocação que conte o número de letras 'a' em 'banana'."""
def count(string: str, letter: str):
    count = 0
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
    return count


word = 'banana'
print(count(word, 'a'))

