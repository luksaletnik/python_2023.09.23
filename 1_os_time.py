import os

print('I am on the path:', os.getcwd())
os.chdir('C:\\Users\\luksa\\PycharmProjects\\pythonProject_2\\python_2023.09.23\\pythonProject_2.1')
# os.chdir(r'C:\Users\luksa\PycharmProjects\pythonProject_2.1')       # r - raw string, alternatywa do powyższego
print('New path:', os.getcwd())

os.mkdir('new_folder')
