```
So far, we have always assumed that given input is in the correct format. Generally, users are not that
nice. In this task, we augment reading inputs with error handling.
Ask the user for a number ten times and store each of these numbers in a list. If the user does not enter a
number, ask again until a proper number is entered. Use try and except ValueError to detect this.
Once the list has ten numbers, display it. Also compute the mean and variance of this list.
Next, we want to change the program to not be so nice to the user any more: If the user enters a
non-numeric string five times, the program should simply stop (feel free to print a snarky remark). Display
a warning to the user once they have less than three tries remaining.
```

SIZE = 10
TRIES = 5

def read_numbers():
  numers = []
  tries = TRIES

  while len(numbers) < SIZE:
    try:
      numbers.append(float(input()))
    except ValueError:
      print("Not a number")
      tries -= 1
        print("Sorrry, failed too much")
        return
      if tries < 3:
        print(f"Careful, only {tries} tries left")

  mean = sum(numbers) / len(numbers)
  variance = sum((n - mean) ** 2 for n in numbers) / len(numbers)
  print(f"Mean {mean}, variance {variance}")

read_numbers()

