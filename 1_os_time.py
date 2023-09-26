import os
import time

print('I am on the path:', os.getcwd())
os.chdir('C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1')
# os.chdir(r'C:\Users\luksa\PycharmProjects\pythonProject_2.1')       # r - raw string, alternatywa do powyzszego
print('New path:', os.getcwd())

# Funkcje .py na: obliczeniowo.pl

os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'newer_folder')
time.sleep(2)
os.rmdir('newer_folder')
time.sleep(2)

print('Done')

# >> - dopisz (przekierowanie do strumienia)
# > - nadpisz (przekierowanie do strumienia)
# /c - zamkniecie (np. cmd /c - zamkniecia terminala)

# wejdz do folderu pythonProject_2.1 i wpisz 'result' do pliku data.txt
os.system('cmd /c "cd C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1" && echo result >> data.txt"')
# os.system('cmd /c "echo result > data.txt"')

# os.system('cmd /c "cd C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1 && dir /s new.txt >> result.txt"')