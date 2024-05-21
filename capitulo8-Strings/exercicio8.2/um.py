def count(string: str, letter: str):
    count = 0
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
    return count


word = 'banana'
print(count(word, 'a'))

