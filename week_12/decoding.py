```
While entering data into an Excel table, an intern unfortunately sometimes entered l (lower case L)
instead of 1 (one), and O (upper case o) instead of 0 (zero). Write a program that reads a sequence
of “numbers” in one line, e.g. 1O 87l2022O Ol12231, fixes the mistakes, and then prints out the fixed
sequence. Read up on the methods split and replace.
Extend your program to also print the average value of the numbers. For example, given the input 1O 1l
l2, your program should print 10 11 12 and Average: 11.0.
PS: We might learn how to directly interact with excel tables in the future. (For the experienced ones:
look up the modules csv and xlsxwriter.)
```

l = inout() .replace("O", "0") .replace("l", "1") .split()
s = 0
for n in l:
  print (n, end = " ")
  s += int(n)
print()
print(f"Average: {s / len(l)}")

                                                                              
