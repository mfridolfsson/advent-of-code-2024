import re

input = open('data.txt', 'r').read()

output = 0

valid_muls_input = []

print(input)
print(" ")
split_dont = re.split("don\'t\(\)", input)
print("split_dont")
print(split_dont) 


#we know item one will always be valid
valid_muls_input.append(split_dont[0])
split_dont.pop(0)

for index, item in enumerate(split_dont):
    print("item")
    print(item)
    print("split_do")
    split_do = re.split("do\(\)", item)
    print(split_do)
    split_do.pop(0)
    #if exixts second item onwards of list will be do onwards1
    print("remove_dont_values")
    print(split_do)
    if len(split_do) > 0:
        valid_muls_input.extend(split_do)
        print(split_do)

print("valid_muls_input")
print(valid_muls_input)

valid_muls_input_str = ''.join(valid_muls_input)

valid_muls = re.findall("mul\(\d+,\d+\)", valid_muls_input_str)

print("valid_muls")
print(valid_muls)

for index, item in enumerate(valid_muls):
    comma_location = re.search(',', item).start()
    first_number = int(item[4:comma_location])
    second_number = int(item[comma_location+1:len(item)-1])
    print(first_number)
    print(second_number)
    output += first_number*second_number

print(output)