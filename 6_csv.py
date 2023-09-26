path = 'rozliczenie.csv'
mode = 'r'  # read - do odczytu (w - write, do zapisu, x - execute, do wykonania, a - append, do dopisania)
with open(path, mode) as my_file:
    content = my_file.readlines()

print(content)

for i in range(len(content)):
    content[i] = content[i].split(',')

print(content)
print(content[3])
print(content[3][2])            # pierwszy index - wiersz, drugi index - kolumna
print(content[0][2][3: -2])     # trzeci index - znaki stringa

# string.replace('\n', '')

print('\n\n')

# word = 'oxo.xoxo'
# word = word.replace('o', 'O', 2)
# print(word)
#
# word = 'oxo.xoxo'
# word = word.split('.')
# print(word)
