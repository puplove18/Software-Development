/*
With the basics established, we now want to use make to compile programs.
Remember how we assemble programs: First, the preprocessor runs, inserting all the headers, then
compilation happens, and then linking. In this exercise, we focus on the first parts, no linking is required.
The program we want to write and compile with just reads in some numbers from the user and prints it,
similar to what we have seen. However, we will spread out the functionality over multiple files.
To start with, create a small utility file util.h, which should contain an array printing function:

  #include <stdio.h>
  void print_array(int *array, int size) {
    // Put printing code here
  }

Next, write code to read n numbers from the user in main.c, similar to:

  int main() {
    int n;
    scanf("%d", &n);
    int *array = malloc(sizeof(int[n]));
    for (int i = 0; i < n; i++) {
      // Read n values in the array
    }
  }

To conclude the “setup”, we want to print the array:

  #include "util.h"
  int main() {
    // previous code
    print_array(array, n);
  }

Compile main.c and see that it works.
Now, we want to automate compilation using a Makefile. Using the terminology of the previous exercise,
the cake would be finished program, flour would be main.c, and wheat the imported header file, since
main.c depends on util.h. Create a Makefile that compiles your program to an executable named main:

  all: // what comes here?
  main: // What are the *direct* dependencies of main?
    // Compile
  clean: // Should clean everything you generate
  .PHONY: // what comes here?

Simply running make in the folder should now compile your file! Check that running make again doesn’t
do anything. Make some changes to main.c or util.h (or touch one of the files) and run make again to
verify the files are compiled again.
*/


all: main 

main: main.c util.h
  gcc -o main main.c

clean: 
  rm main

.PHONY: all












Bonus: Compile the file with additional flags, such as -O2 -Wall -Werror.
