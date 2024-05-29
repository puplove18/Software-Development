```
Write function def is_prime(n), which returns whether the integer n and is a prime or not. For example,
for 3, 5, and 2971215073, it should return True; for 4, 10, or 10203501230 it should return False.
Extend your program to read an integer from the user and print whether it is a prime or not.
Again extend your program to read an integer from the user and instead print all primes that are smaller
than the given number.
```

def is_prime(n):
  if n == 2:
    return True
  if n <= 1 or n % 2 == 0:
    return False
  i = 3
  while i * i < n:
    if n % i == 0:
      return False
    i += 1
  return True

num = int(input("Please enter a number: "))
print(f"Primes smaller than{num}:")
for i in range(2, num):
  if is_prime(i):
    print(i)
