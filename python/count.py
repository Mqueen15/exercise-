def count_ch(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total

print(count_ch('hello world', 'o'))
print(count_ch('hello world', 'a'))
