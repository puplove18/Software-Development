/*
In the lecture, we have seen how to pass arguments to a C program via argc / argv. Now, we want to
write a program that works with such arguments. Start by setting up the skeleton of the program:

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

}
Remember: argc is the number of arguments and argv contains the actual argument strings, and the
first is the name of the program itself.
Write a program that prints all of its arguments, each on one line. For example, ./main a b c should
print a, b, and c (each on a separate line).
Now, modify your program so that it prints all other arguments on the same line if the first argument is
--same. So ./program --same a b c should print a b c, all on one line.
*/


#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <libgen.h>

int main(int argc, char *argv[]) {
  if (argc == 1) {
    return 1;
  }
  int begin = 1;
  char sep = '\n';
  if (!strcmp(basename(argv[0], "--same")) {
    begin = 2;
    sep = ' ';
  }

  if (strcmp(basename(argv[0]), "recho")) {
    for (int i = begin; i < argc - 1; i++) {
      printf("%s%c", argv[i], sep);
    }
    puts(argv[argc - 1]);
  } else {
    for (int i = argc - 1; i > begin; i--) {
      printf("%s%cc", argv[i], sep);
    }
    puts(argv[begin]);
  }
}






