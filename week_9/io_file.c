/*
For the second part, we want to work with file input and output. Our goal will be to reverse the lines of a
file and write the reversed contents to another file. Our first step is to open and read the file, which we
want to be given as command line argument. Proceed in the following steps:

  • Create a file text and write some text in it.
  • Write a program that opens the file text using fopen, check that opening the file worked, and close
  the file again.
  • With the file correctly opened and closed, read the first 10 characters from the file using fgets, and
  print them to the console.
  • Instead of opening text, take the name from the command line arguments.
  • Now, read the file in full, printing its contents to the console (you just implemented cat!)
  • Since we want to reverse the order of the lines, read the contents of the file line by line, store them
  in a list / stack, and print out the lines in reverse order.
  • To conclude, instead of printing the reversed lines to the console, print them to a file specified as
  the second argument.

In summary, if the contents of text are

  one line
  second line
  Hello

and you run main text text-rev, the contents of text-rev should be
  
  Hello
  second line
  one line


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <libexplain/fopen.h>

char *read_line(FILE *file, char **dest) {
  int pos = 0;
  int size = 8;
  char *line = malloc(sizeof(char[size]));
  while (true) {
    char c = fgetc(file);
    if (c == '\n' || c == EOF) {
      line[pos] = '\0';
      *dest = line;
      return c == EOF ? NULL : line;
    }
    line[pos] = c;
    pos += 1;
    if (pos == size) {
      size *= 2;
      line = realloc(line, sizeof(char[size]));
    }
  }
}

int main(int argc, char *argv[]) {
  if (argc < 2 || argc > 3) {
    fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  FILE *fin = explain_fopen_or_die(argv[1], "rt");
  FILE *fout = argc == 2 ? stdout : explain_fopen_or_die(argv[2], "wt");

  int pos = 0;
  int size = 8;
  char **array = malloc(sizeof(char *[8]));
  while (true) {
    if (!read_line(fin, array + pos)) {
      break;
    }
    pos += 1;
    if (pos == size) {
      size *= 2;
      array = realloc(array, sizeof(char *[size]));
    }
  }
  fclose(fin);

  for (int i = pos - 1; i >= 0; i--) {
    fputs(array[i], fout);
    fputc('\n', fout);
  }
}







