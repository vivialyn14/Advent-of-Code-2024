with open("puzzle_input.txt") as fh:
  puzzle_input = fh.read()

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

left_list = []
right_list = []
index = 0
answer = 0

lines = puzzle_input.splitlines()
for line in lines:
  x, y = line.split()
  left_list.append(int(x))
  right_list.append(int(y))

left_list.sort()
right_list.sort()

for i in left_list:
  if i in right_list:
    answer += i * right_list.count(i)

print(answer)