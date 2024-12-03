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

for left_index, left_item in enumerate(left):
    left_num = int(left_item)
    for right_index, right_item in enumerate(right):
        right_num = int(right_item)
        if left_num == right_num:
            output += left_num

print(output)
