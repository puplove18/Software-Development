```
1. First, create a list containing the numbers 1 to 10 using a literal expression (l = [...]). Print the
list an see that it contains the numbers.
2. Then, create the same list using list and range. Can you also use range and a list comprehension?
3. Using the list you created in the above steps, create a list containing the string Number: <i> for
each number in the list. So, the list should look like ["Number: 0", "Number: 1", ...]. Try to
create this list using both a for-loop and list comprehension.
4. Create the same list, but only containing even numbers. Try different approaches, using slicing,
range, or list comprehension.
5. Use join to connect this list of strings to a single string, separated by semicolon ;, and print it.
The output should look like "Number: 0; Number: 2; ...".
6. Use list comprehension to create the list of all square numbers from 1 to n.
```

print("; ".join([f"Number: {1}" for i in range(1. 10) if i % 2 == 0])
n = int(input())
squares = [i * i for  i in ramge(n)]
