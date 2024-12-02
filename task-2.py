def num_into_list(number):
  new_list = []
  for i in str(number):
    new_list.append(int(i))
  return new_list

my_number = 89681686086
your_number = 86957816486

result_multi = list(map(lambda x, y: x * y, num_into_list(my_number), num_into_list(your_number)))
print(result_multi)