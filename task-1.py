def multiply_fun(x, variant):
  return x * (variant + 3)

elements = [12, 24, 36, 48, 109, 187];
my_variant = 18

print(list(map(lambda x: multiply_fun(x, my_variant), elements)))

lambda_fun = list(map(lambda x: x * 21, elements));

print(lambda_fun)