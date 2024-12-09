import re

input = open('data.txt', 'r').read()

output = 0

print(input)

valid_muls = re.findall("mul\(\d+,\d+\)", input)

print(valid_muls)

for index, item in enumerate(valid_muls):
    comma_location = re.search(',', item).start()
    first_number = int(item[4:comma_location])
    second_number = int(item[comma_location+1:len(item)-1])
    print(first_number)
    print(second_number)
    output += first_number*second_number

print(output)