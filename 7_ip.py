import os

# os.system('cmd /c "cd C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1" && ipconfig /all > ip_data.txt"')

os.system(' cmd /c "ipconfig /all > ip_data.txt" ')

path = 'ip_data.txt'
mode = 'r'  # read - do odczytu (w - write, do zapisu, x - execute, do wykonania, a - append, do dopisania)
with open(path, mode, encoding="utf8", errors="ignore") as txt_file:
    content = txt_file.readlines()

number_line = 0
for i in range(len(content)):
    if '(Preferred)' in content[i]:
        content[i] = content[i].split(':')
        number_line = i

print(content[number_line][1][1: -13])
