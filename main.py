string_input = [int(i) for i in input().split()]
list1 = []
string_input.sort()
length_string = len(string_input) - 1
k = 100000
if len(string_input) != 1:
    for i in range(0, length_string):
        if string_input[i] == string_input[i+1] and string_input[i] != k:
            list1.append(string_input[i])
            k = string_input[i]
    for j in range(length_string, length_string + 1):
        if string_input[-1] == string_input[-2] and string_input[j] != k:
            list1.append(string_input[j])
length_arr = len(list1)
for g in range(0, length_arr):
    print(list1[g], end=' ')
