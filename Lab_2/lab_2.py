#Part 1 
#Take the following list and multiply all list items together.

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

part1_result = 1

for i in part1:
    part1_result *= i

print("%s is the result of part 1" %part1_result)

#Part 2 
#Take the following list and add all list items together.

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

part2_result = 0

for i in part2:
    part2_result += i

print("%s is the result of part 2" %part2_result)

#Part 3 
#Take the following list and only add together those list items which are even.

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

part3_result = 0

for i in part3:
    if i % 2 == 0:
        part3_result += i

print("%s is the result of part 3" %part3_result)
