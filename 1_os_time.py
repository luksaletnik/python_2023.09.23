import os
import time

print('I am on the path:', os.getcwd())
os.chdir('C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1')
# os.chdir(r'C:\Users\luksa\PycharmProjects\pythonProject_2.1')       # r - raw string, alternatywa do powyższego
print('New path:', os.getcwd())

# Funkcje py na: obliczeniowo.pl

os.mkdir('new_folder')
time.sleep(2)
os.renames('new_folder', 'newer_folder')
time.sleep(2)
os.rmdir('newer_folder')
time.sleep(2)

print('Done')

# >> - przekierowanie do strumienia

os.system('cmd /c "cd C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1 && dir /s new.txt >> result.txt"')