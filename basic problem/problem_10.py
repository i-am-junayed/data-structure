def is_prime(num):
  if num <= 1:
    return False
  else:
    for i in range(2, num, 1):
      if num % i == 0:
        return False
  return True

my_list = [23, 12, 54, 7, 19]
count = 0
for i in my_list:
  if (is_prime(i)):
    count = count + 1
print(f'There are {count} prime numbers in the list')
