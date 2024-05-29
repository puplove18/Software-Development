/*
To learn why we actually want to use Makefiles, we want to create a more slightly more involved, multi-file
project. We want to use the following layout:

  project/
    lib/
      util.h
      stack.h
    src/
      stack.c
    main.c

Here, stack.h and stack.c should define and implement a simple array-based stack, as we have already
seen. The util.h file should contain the same content as in the previous exercise, namely a function to
print an array.
Now we define stack.h. Recall from the lecture that in the header file we only want to define the functions,
not implement them.

  struct stack;
  struct stack *make_stack();
  void free_stack(struct stack *s);
  void print_stack(struct stack *s);
  // Define some more, at least push and pop

Next, we want to implement these functions. Do this by creating stack.c and filling it appropriately:

  #include "stack.h"
  #include "util.h"
  #include <stdlib.h>

  struct stack {
    int top; // Where is the first free element
    int size; // Size of the array
    int *array; // Store the data
  };
  struct stack *make_stack() {
    struct stack *s = malloc(sizeof(struct stack));
    s->top = 0;
    // Complete this
  }
  void print_stack(struct stack *s) {
    printf("STACK ");
    // Use the print function we defined in util!
    print_array(s->array, s->top);
  }
  // Implement the other functions

With this ready, we now want to compile our implementation of the stack – but not produce an executable.
Recall: -c tells gcc to only compile, not link, and -I specifies folders to search for included .h files. Your
command should look somewhat like this: gcc <arguments> src/stack.c and, on completion, produce
stack.o in the main folder of the program.
Next, we define the main function, which should now use a stack:

  #include "util.h"
  #include "stack.h"
 
  // and more
  int main() {
    struct stack *s = make_stack();
    int n;
    scanf("%d", &n);
    int *array = malloc(sizeof(int[n]));
    for (int i = 0; i < n; i++) { // Read n numbers and push them on the stack
      int in;
      scanf("%d", &in);
      push_stack(s, in);
    }
    print_stack(s);
    for (int i = 0; i < n; i++) {
      printf("%d", pop_stack(s));
    }
  }

If we would simply compile this file, everything would work. (What would happen if you remove the
#include "stack.h" ?) However, in the linking step, we would discover that an implementation of, e.g.,
make_stack is missing. We need to tell the compiler where to get these. Compile your program with gcc
<arguments> main.c stack.o (the stack.o tells the compiler to search for symbols in that file).
Now, we are ready to start the Makefile-part of the exercise. Your goal now is to define a proper makefile
to compile this program automatically. In particular, stack.o should only be regenerated if something in
stack.h, stack.c, or util.h changes! You may start from the following template:

  all: main
  main: main.c // What other direct dependencies are there?
    @echo "Compile main"
    // compile main.c to main
  stack.o: // Which dependencies?
    @echo "Compile stack"
    // compiling stack.o
  clean:
    // what should we clean?
  .PHONY: // ...

Check the compilation works, modify some files and run make again to see what is compiled. Are the
right things being compiled?
*/
<solution>

all: main

build:
  mkdir -p build

main: build main.c build/stack.o lib/util.h lib/stack.h
  @echo "Compile main"
  gcc -o build/main -Ilib build/stack.o main.c

build/stack.o: build lib/util.h lib/stack.h src/stack.c
  @echo "Compile stack"
  gcc -o build/stack.o -c -Ilib src/stack.c

# Would need to change the build command above with -lstack -Lbuild
build/libstack.a: build build/stack.o
  ar -rcs build/libstack.a build/stack.o

clean:
  rm -fr build

.PHONY: all

can you explain the solution?
