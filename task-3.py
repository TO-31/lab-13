my_num = [8, 9, 6, 8, 1, 6, 8, 6, 0, 8, 6]

multi = list(map(lambda x: x * 19, my_num))

even_num = list(filter(lambda x: x % 2 == 0, multi))
odd_num = list(filter(lambda x: x % 2 != 0, multi))

print(f"{even_num}\n{odd_num}")