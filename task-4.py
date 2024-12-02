my_num = ["8", "9", "6", "8", "1", "6", "8", "6", "0", "8", "6"]

refreshed = list(map(lambda x: int(x), my_num))
refreshed_celochislenoy = list(map(lambda x: x // 18, refreshed))
refreshed_drobi = list(map(lambda x: x / 18, refreshed))

print(refreshed)
print(refreshed_celochislenoy)
print(refreshed_drobi)