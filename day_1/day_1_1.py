with open('data.txt', 'r') as f:
   lines = f.read().split('\n')

left = []
right = []

const_num_len = 5

for line in lines:
  left.append(line[:const_num_len])
  right.append(line[-const_num_len:])

left.sort()
right.sort()

output = 0

for index, item in enumerate(left):
    left_num = int(item)
    right_num = int(right[index])
    output = output + (abs(left_num-right_num))

print(output)
