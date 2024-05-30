```
  For help, you can also have a look at the argparse tutorial (https://docs.python.org/3/howto/argparse.html#argparse-tutorial).
Define a command line interface using argparse. Create a parsers with argparse.ArgumentParser(...) and
add a (positional) argument named filename to it with .add_argument(...). Finally, parse the arguments
with args = parser.parse_args(). To verify that your implementation works, print args.filename and
run your program by python main.py foo.
Next, we want to add some functionality. Try to open a file at the path given by the user and print its
contents to the console. Run your program and give it a file as argument, e.g. python main.py main.py.
See what happens if you specify a non-existent file, e.g. python main.py foobarspameggs.xyz.
Now, we want to make our program configurable. Add an option --count. If the given value is lines,
instead of printing the text, your program should output the number of lines in the file. Similarly, if the
value is words or characters, print the appropriate amount.
```
  
import argparse
import pathlib

def main(args):
  with args.file.open(mode="rt") as f:
    if args.count:
      c: int = 0
      if args.count == "lines":
        for _ in f:
          c += 1
      elif args.count == "words":
        for line in f:
          c += len(line.split())
      elif args.count == "characters":
        for line in f:
          c += len(line)
      print(c)
    else:
      for line in f:
        print(line[:-1])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("file", type=pathlib.Path)
  parser.add_argument("--count", choices=["lines", "words", "characters"])
  main(parser.parse_args())
