path = 'my_file.txt'
mode = 'r'  # read - do odczytu (w - write, do zapisu, x - execute, do wykonania, a - append, do dopisania)
with open(path, mode) as txt_file:
    # content1 = txt_file.read()      # przeczyta wszystko

    # content2_1 = txt_file.read(5)   # przeczytaj 5 pierwszych/kolejnych
    # content2_2 = txt_file.read(5)

    content3 = txt_file.readlines()

# print(content1)
# print(type(content1))
# print(content2_1)
# print(content2_2)
print(content3)
print(type(content3))
