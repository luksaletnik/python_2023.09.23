string_1 = 'word1'
string_2 = 'word2'

string_sum = string_1 + ' and ' + string_2

print(string_sum)

print(string_sum[2: 6])
print(string_sum[: 6])
print(string_sum[2:])
print(string_sum[2: -6])

list_1 = ['word_1', 'word_2', 123, 321.123]
print(list_1)
print(list_1[1: 3])
print(list_1[1: -1])
print(list_1[1:])

print(list_1[1][1: 4])
print(list_1[1][1: 4] + list_1[0][: 3])
